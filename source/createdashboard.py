import psycopg2
import time

class Database:
	def __init__(self):
		self.conn = self.connectDB()

	def connectDB(self):
		conn = psycopg2.connect(host='127.0.0.1', dbname='everest_db_bkp', user='everest', password='EveIMS@121$')
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

class CreateDashboard:
	def __init__(self):
		self.database = Database()

	def getDasboardsCreated(self):
		# last_id = None
		# last_id_qry = 'select id from tbldashboard order by id desc limit 1;'
		# last_id_obj = self.database.executeSQLStatement(last_id_qry)
		# if len(last_id_obj):
		# 	last_id = int(last_id_obj[0].get('id', 0))

		f = open('dashboardbackup_bdc.dat')
		backup_dataset = eval(f.read())
		f.close()
		self.database.executeSQLStatement(backup_dataset.get('INSERT_QRY_DASHBOARD',''))

		data_dict = backup_dataset.get('DATA_DICT','')
		dashboard_dict = data_dict.get('dashboard_dict','')
		widget_dict = data_dict.get('widget_dict','')
		dash_opts_dict = data_dict.get('dash_opts_dict','')

		final_dw_qry = ''
		for k, v in dashboard_dict.iteritems():
		    v.update({'widgets':widget_dict.get(k,[])})

		for k, v in dashboard_dict.iteritems():
		    dw_col_list = v['widgets']
		    for w in dw_col_list:
		        qry_widget_id = "select id from tblwidget where name = '%s';" % w.get('widget','')
		        res_widget_id = self.database.executeSQLStatement(qry_widget_id)
		        w.update({'widget':res_widget_id[0].get('id',None)})
		        qry_dash_id = "select id from tbldashboard where name = '%s';" % (k)
		        res_dash_id = self.database.executeSQLStatement(qry_dash_id)
		        w.update({'dashboard':res_dash_id[0].get('id',None)})
		        dw_col_list = w.keys()
		        dw_col_str = str(dw_col_list)[1:-1]
		        dw_col_str = dw_col_str.replace("'","")
		        dw_col_str = dw_col_str.replace('column','"column"')
		        dw_col_str = dw_col_str.replace('row','"row"')
		        dw_val_list = w.values()
		        dw_val_str = str(dw_val_list)[1:-1]
		        dw_val_str = dw_val_str.replace("None","NULL")
		        dw_val_str = dw_val_str.replace("u'","'")
		        dw_val_str = dw_val_str.replace("'now()'","now()")
		        dw_qry = 'INSERT INTO tbldashboardwidget (%s) VALUES (%s);' % (dw_col_str, dw_val_str)
		        final_dw_qry = final_dw_qry + dw_qry + '\n'

		self.database.executeSQLStatement(final_dw_qry)

		final_dbopts_qry = ''
		qry_db_opts = "select dw.id, d.name as db_name, w.name as widget, dw.row, dw.column from tbldashboard d, tblwidget w, tbldashboardwidget dw where d.id=dw.dashboard and w.id=dw.widget;"
		res_db_opts = self.database.executeSQLStatement(qry_db_opts)
		for data in res_db_opts:
		    for k,v in dash_opts_dict.iteritems():
		        if k == (data.get('db_name'), data.get('row'), data.get('column')):
		            qry_wid_id = "select id from tblwidget where name = '%s';" % v[0].get('widget','')
		            res_wid_id = self.database.executeSQLStatement(qry_wid_id)
		            qry_db_id = "select id from tbldashboard where name = '%s';" % (v[0].get('db_name',''))
		            res_db_id = self.database.executeSQLStatement(qry_db_id)
		            qry_dw_id = "select id from tbldashboardwidget dw where dw.dashboard = %s and dw.row = %s and dw.column = %s;" % (res_db_id[0].get('id'), data.get('row'), data.get('column'))
		            res_dw_id = self.database.executeSQLStatement(qry_dw_id)
		            v[0].update({'widget':res_wid_id[0].get('id', None)})
		            v[0].update({'dashboard':res_db_id[0].get('id', None)})
		            v[0].update({'dashboardwidget': res_dw_id[0].get('id', None)})
		            del v[0]['column']
		            del v[0]['row']
		            del v[0]['db_name']
		            dbopts_col_list = v[0].keys()
		            dbopts_col_str = str(dbopts_col_list)[1:-1]
		            dbopts_col_str = dbopts_col_str.replace("'", "")
		            dbopts_val_list = v[0].values()
		            dbopts_val_str = str(dbopts_val_list)[1:-1]
		            dbopts_val_str = dbopts_val_str.replace("None", "NULL")
		            dbopts_val_str = dbopts_val_str.replace("u'", "'")
		            dbopts_val_str = dbopts_val_str.replace("'now()'", "now()")
		            dbopts_qry = 'INSERT INTO tbldashboardoptions (%s) VALUES (%s);' % (dbopts_col_str, dbopts_val_str)
		            final_dbopts_qry = final_dbopts_qry + dbopts_qry + '\n'

		self.database.executeSQLStatement(final_dbopts_qry)


qry_obj = CreateDashboard()
qry_obj.getDasboardsCreated()
