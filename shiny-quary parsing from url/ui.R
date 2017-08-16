library(shiny)

shinyUI(fluidPage(
  # textInput("x", "Symbol Entry", ""),
  # textInput("y", "Symbol Entry", "")
  
  
  #dateInput("date_start", h4("Start Date"), value = "2005-01-01" ,startview = "year"),
  
  # selectInput("period_select", label = h4("Frequency of Updates"),
  #             c("Monthly" = 1,
  #               "Quarterly" = 2,
  #               "Weekly" = 3,
  #               "Daily" = 4)),
  # 
   sliderInput("a", label = "SMA Len",min = 1, max = 200, value = 115),br(),
   sliderInput("b", label = "SMA Len",min = 1, max = 200, value = 115),br(),
  
  # 
  # checkboxInput("usema", "Use MA", FALSE)
  


mainPanel(
    "Summary",verbatimTextOutput('contents11')
    
))
)
