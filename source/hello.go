package main
import "fmt"

func main(){
	data := "Hello, World!"
	for i := 1; i <= 5; i+=1 {
		fmt.Println(myfunc(data, i))
	}
}

func myfunc(data string, i int) (res1 string, res2 int) {
	fmt.Println(data)
	new_data := "It's Sahas"
	res1 = new_data
	res2 = i
	return
}