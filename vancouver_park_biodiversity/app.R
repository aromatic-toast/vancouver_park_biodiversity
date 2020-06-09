#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)


# Define UI for application that draws a histogram
members <- data.frame(name=c("Name 1", "Name 2"), nr=c('BCRA1','FITM2'))

ui <- fluidPage(titlePanel("Getting Iframe"), 
                sidebarLayout(
                    sidebarPanel(
                        fluidRow(
                            column(6, selectInput("Member", label=h5("Choose a option"),choices=c('BCRA1','FITM2'))
                            ))),
                    mainPanel(fluidRow(
                        htmlOutput("frame")
                    )
                    )
                ))

server <- function(input, output) {
    observe({ 
        query <- members[which(members$nr==input$Member),2]
        test <<- "https://www.amazon.ca/gp/product/B01IG6C0D4/ref=s9_acsd_top_hd_bw_b7FtldL_c_x_w?pf_rd_m=A1IM4EOPHS76S7&pf_rd_s=merchandised-search-11&pf_rd_r=WGWCDV8ZX4301B1JV1MY&pf_rd_t=101&pf_rd_p=63b2d8a9-07e3-5379-aa11-08da2e8ae607&pf_rd_i=6647866011"
    })
    output$frame <- renderUI({
        input$Member
        my_test <- tags$iframe(src=test, height=600, width=535)
        print(my_test)
        my_test
    })
}


# Run the application 
shinyApp(ui = ui, server = server)


