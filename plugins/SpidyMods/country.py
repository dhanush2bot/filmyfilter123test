from countryinfo import CountryInfo
from pyrogram import filters, Client 
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests
import wikipediaapi

# Create a Wikipedia API client for English Wikipedia
wiki_api = wikipediaapi.Wikipedia('en', user_agent='MyBot/1.0')

@Client.on_message(filters.command(["country"]))
async def country_info(bot, update):
    country_name = update.text.split(" ", 1)[1]
    country_info = CountryInfo(country_name)
    
    # Use the Wikipedia API to fetch a summary of the country
    wiki_page = wiki_api.page(country_name)
    wiki_summary = wiki_page.summary[:1000]  # Limit the summary to 1000 characters
    
    # Additional information
    languages = country_info.languages()
    flag_url = f"https://www.countryflags.io/{country_info.iso_alpha2()}/flat/64.png"
    map_url = f"https://www.google.com/maps/place/{country_info.capital()}"
    
    # Fetch currency exchange rates using an API
    currency_api_url = f"https://api.currencylayer.com/live?access_key=YOUR_ACCESS_KEY&source=USD&currencies={country_info.currency_iso()}"
    response = requests.get(currency_api_url)
    exchange_rates = response.json()['quotes']
    country_currency = country_info.currency()
    exchange_rate = exchange_rates[f"USD{country_currency}"]
    
    # Fetch COVID-19 statistics using an API
    covid_api_url = f"https://disease.sh/v3/covid-19/countries/{country_name}"
    response = requests.get(covid_api_url)
    covid_data = response.json()
    total_cases = covid_data['cases']
    total_deaths = covid_data['deaths']
    total_vaccinations = covid_data['vaccinations']
    
    # Construct the information message
    info = f"""𝖢𝗈𝗎𝗇𝗍𝗋𝗒 𝖨𝗇𝖿𝗈𝗋𝗆𝖺𝗍𝗂𝗈𝗇
𝖭𝖺𝗆𝖾 : {country_info.name()}
𝖭𝖺𝗍𝗂𝗏𝖾 𝖭𝖺𝗆𝖾 : {country_info.native_name()}
𝖢𝖺𝗉𝗂𝗍𝖺𝗅 : {country_info.capital()}
Population : <code>{country_info.population()}</code>
𝖱𝖾𝗀𝗂𝗈𝗇 : {country_info.region()}
𝖲𝗎𝖻 𝖱𝖾𝗀𝗂𝗈𝗇 : {country_info.subregion()}
𝖳𝗈𝗉 𝖫𝖾𝗏𝖾𝗅 𝖣𝗈𝗆𝖺𝗂𝗇𝗌 : {country_info.tld()}
𝖢𝖺𝗅𝗅𝗂𝗇𝗀 𝖢𝗈𝖽𝖾𝗌 : {country_info.calling_codes()}
𝖢𝗎𝗋𝗋𝖾𝗇𝖼𝗂𝖾𝗌 : {country_info.currencies()}
𝖱𝖾𝗌𝗂𝖽𝖾𝗇𝖼𝖾 : {country_info.demonym()}
𝖳𝗂𝗆𝖾𝗓𝗈𝗇𝖾 : <code>{country_info.timezones()}</code>
Official Language(s): {', '.join(languages)}
Wikipedia Summary: {wiki_summary}
Currency Exchange Rate (1 USD = {exchange_rate} {country_currency})
COVID-19 Statistics:
- Total Cases: {total_cases}
- Total Deaths: {total_deaths}
- Total Vaccinations: {total_vaccinations}
"""

    # Buttons
    buttons=[
        [InlineKeyboardButton("ᴡɪᴋɪᴘᴇᴅɪᴀ", url=wiki_page.fullurl)],
        [InlineKeyboardButton("ɢᴏᴏɢʟᴇ", url=f"https://www.google.com/search?q={country_name.replace(' ', '+')}")],
        [InlineKeyboardButton("Map Location", url=map_url)],
        [InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close_data')]
    ]

    try:
        await update.reply_photo(
            photo=flag_url,
            caption=info,
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
    except Exception as error:
        await update.reply_text(
            text=error,
            disable_web_page_preview=True,
            quote=True
        )
