# Microsoft Edge Collections Downloader

If you, like me, started panicking one day in June 2026 because you couldn't find the Collections button on Microsoft Edge anymore, don't despair! This script uses [Playwright](https://playwright.dev/python/docs/intro) to log into your Microsoft account and extract data from the [Bing Collections page](https://bing.com/saves) where all your Collections are still stored.


  
# ...but why? 
Like they did with many of my favourite things (massive shoutout to [Clippy](https://www.artsy.net/article/artsy-editorial-life-death-microsoft-clippy-paper-clip-loved-hate)) Microsoft decided to take Collections too away from me.  
  
Introduced in the pretty eventful (eventless?) year of the lord 2020, Collections have since been my ADHD comfort blanket, always ready to give a semblance of order in my chaotic internet life. In the past 6 years, I collected 100+ link-filled folders, one for each of my special and volatile interests. I have rarely gone back to them (hi _Marimo Moss Balls_ collection! [Fig. 1]), but knowing they were there gave me solace.

<p align="center">
  <img width="264" height="36" alt="image" src="https://github.com/user-attachments/assets/e66b0bc9-68f7-42a9-9017-cba1b464ad12"/>
</p>
<p align="center"><sup><sub>Figure 1. Marimo Moss Balls collection being scraped by my Microsoft Edge Collections Downloader</sub></sup></p>


# Here's what to do in three easy steps:

1. Run the script and wait for a new browser page to open.

2. Sign in to your Microsoft account and get rid of any pop-ups.
   Don't click on anything else on the page.
   
4. Return to the script and press Enter.

..._et voilà_! 🪄

The script first prints a list of all your collections with their respective IDs and number of items. It then exports your data in both a .csv and an .html file containing a list of all your Collections, including links.  
  
The HTML file is bookmarks-readable, meaning you can import it in your preferred browser's (I won't blame you if you've decided not to use Edge anymore) Favourites/Bookmarks.  
  
FYI Edge put my Collections under 'Other Favourites' and it took me way longer than I'd like to admit to find them after import -.-"

Hope this was helpful to some of you Collections _aficionados_.
