import psycopg2

class Database:
	def __init__(self):
		self.conn = self.connectDB()

	def connectDB(self):
		conn = psycopg2.connect(host='192.168.50.130', dbname='everest_db', user='everest', password='EveIMS@121$')
		return conn

	def executeSQLStatement(self, sql_stmt):
		try:
			cursor = self.conn.cursor()
			retValue = cursor.execute(sql_stmt)
			out = -1
			if cursor.description:
				colnames = [x[0] for x in cursor.description]
				out = cursor.fetchall()
				for i in xrange(len(out)):
					out[i] = dict(zip(colnames, out[i]))
			else:
				if retValue == -1:
					out = -1
			return out
		finally:
			self.conn.commit()
			cursor.close()

class BackupDashboard:
	def __init__(self):
		self.database = Database()

	def classify_objs(self, objs, function):
	    ret = {}
	    for obj in objs:
	        tag = function(obj)
	        if tag not in ret:
	            ret[tag] = []
	        ret[tag].append(obj)
	    return ret

	def getDasboardsBackup(self):
		f = open('dashboardbackup_130_test.dat', 'w')
		dashboard_dict = {}
		query_dashboard = "select * from tbldashboard;"
		res_dashboard = self.database.executeSQLStatement(query_dashboard)
		query_all_db = "select d.name as db_name, w.name as widget, dw.width, dw.height, dw.row, dw.column, dw.autoreload, dw.lastupdatetime, dw.creationtime, dw.isdeleted from tbldashboardwidget dw, tblwidget w, tbldashboard d where dw.widget = w.id and d.id = dw.dashboard;"
		res_all_db = self.database.executeSQLStatement(query_all_db)
		dash_opts_qry = "select d.name as db_name, w.name as widget, dw.row, dw.column, dopt.lastupdatetime, dopt.creationtime, dopt.isdeleted, dopt.displayoptions, dopt.dataoptions, dopt.linkoptions from tbldashboardwidget dw, tblwidget w, tbldashboard d, tbldashboardoptions dopt where dw.widget = w.id and d.id = dw.dashboard and dopt.dashboardwidget = dw.id;"
		res_dash_opts = self.database.executeSQLStatement(dash_opts_qry)
		widget_dict = self.classify_objs(res_all_db, lambda x: x.get('db_name'))
		dash_opts_dict = self.classify_objs(res_dash_opts, lambda x: (x.get('db_name'), x.get('row'), x.get('column')))

		for k, v in widget_dict.iteritems():
		    for data in v:
		        del data['db_name']
		        data.update({'lastupdatetime':'now()'})
		        data.update({'creationtime':'now()'})

		for k, v in dash_opts_dict.iteritems():
		    for data in v:
		        data.update({'lastupdatetime':'now()'})
		        data.update({'creationtime':'now()'})

		for val in res_dashboard:
		    del val['id']
		    del val['updator']
		    val.update({'users':'[]'})
		    val.update({'groups':'[]'})
		    val.update({'lastupdatetime':'now()'})
		    val.update({'creationtime':'now()'})
		    val.update({'creator':1})
		    dashboard_dict.update({val.get('name',''):val})

		final_dashboard_qry = ''
		for k, v in dashboard_dict.iteritems():
		    dash_col_list = v.keys()
		    dash_col_str = str(dash_col_list)[1:-1]
		    dash_col_str = dash_col_str.replace("'","")
		    dash_val_list = v.values()
		    dash_val_str = str(dash_val_list)[1:-1]
		    dash_val_str = dash_val_str.replace("None","NULL")
		    dash_val_str = dash_val_str.replace("u'","'")
		    dash_val_str = dash_val_str.replace("'now()'","now()")
		    dashboard_qry = 'INSERT INTO tbldashboard (%s) VALUES (%s);' % (dash_col_str, dash_val_str)
		    final_dashboard_qry = final_dashboard_qry + dashboard_qry

		dashboard_dataset = {}
		dashboard_dataset.update({"dashboard_dict":dashboard_dict, "widget_dict":widget_dict, "dash_opts_dict":dash_opts_dict})
		final_dict = {}
		final_dict.update({'DATA_DICT': dashboard_dataset, 'INSERT_QRY_DASHBOARD':final_dashboard_qry})
		f.write('%s' % final_dict)
		f.close()

qry_obj = BackupDashboard()
qry_obj.getDasboardsBackup()
