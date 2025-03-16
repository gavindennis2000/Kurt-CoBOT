# Kurt-CoBOT
 A lame Discord bot that matches user messages to Nirvana lyrics then prints them out.

 How to use
    1. Clone the git repository
    2. In this directory create a .env file with the following line of code:
        DISCORD_TOKEN=<insert the discord token here>

I got the Nirvana lyrics dataset from Kaggle in the form of a CSV file and hard-converted
it into a JSON. Then I removed as many songs with profane lyrics as I could. Here is the
link to the original source: https://www.kaggle.com/datasets/darkrubiks/nirvana-lyrics

Prompt engineering with ChatGPT allowed me to use Python data parsing functionality that 
I wasn't familiar with. 

Original image sources:
Discord Bot Profile Picture
    https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2Fgrunge-and-that--862157922424335275%2F&psig=AOvVaw3M0B09EiCOk1oBBe8H_WYO&ust=1742237394380000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCIil25uij4wDFQAAAAAdAAAAABAE
Discord Bot Banner
    https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.theguardian.com%2Fmusic%2F2021%2Foct%2F07%2Fthe-cover-is-supposed-to-be-provocative-the-daunting-task-of-redesigning-nirvanas-nevermind&psig=AOvVaw1nnxfys3nGyypH_NZyCn3N&ust=1742237413655000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJC4lKeij4wDFQAAAAAdAAAAABAE