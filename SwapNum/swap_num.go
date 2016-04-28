package main

import "fmt"
import "bufio"
import "regexp"

func main() {
	file, err := os.Open(os.Args[2])
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		re := regexp.Compile("([0-9]+)([A-Za-z]*)([0-9])")
		fmt.Println(re.ReplaceAllString(scanner.Text, "$3$2$1"))
	}
}
