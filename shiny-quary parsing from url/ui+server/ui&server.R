ui <- bootstrapPage(
   #h3("groupId"),
   verbatimTextOutput("queryText")
)

server <- function(input, output, session) {
  output$queryText <- renderText({
    query <- parseQueryString(session$clientData$url_search)
    a<-paste(query, sep = "", collapse=", ")
    b<-strsplit(a,split = ",")
    as.numeric(b[[1]][2])+as.numeric(b[[1]][1])
    
  })
}

shinyApp(ui = ui, server = server)

#http://127.0.0.1:6317/?a=1&b=2