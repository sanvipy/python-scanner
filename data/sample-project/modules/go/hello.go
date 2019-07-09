package main

import (
	"fmt"
	"net/http"
)

func main() {
	//TODO: Update the message
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello, you've requested: %s\n", r.URL.Path)
	})
	
	//FIXME: Serve through 443 instead
	http.ListenAndServe(":80", nil)
}