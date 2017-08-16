shinyServer(function(input, output,session) {
  observe({
    query <- parseQueryString(session$clientData$url_search)
    
    for (i in 1:(length(reactiveValuesToList(input)))) {
      nameval = names(reactiveValuesToList(input)[i])
      valuetoupdate = query[[nameval]]
      
      if (!is.null(query[[nameval]])) {
        if (is.na(as.numeric(valuetoupdate))) {
          updateTextInput(session, nameval, value = valuetoupdate)
        }
        else {
          updateTextInput(session, nameval, value = as.numeric(valuetoupdate))
        }
      }
      
    }
    
  })
  output$contents11 <- renderPrint({
    
    a <- input$a + input$b

    return(a)    
    
  })
  
})


