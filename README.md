This is a small helper program that makes scraping game information from the website "howlongtobeat.com". The user only needs to provide the name of the game that they wish to look up and the module will return a dictionary with the games details.

I leave it up to the site to do best effort on game matching. If a game cannot be found, a dictionary with an `error` key pair will be returned.

### Usage
The script can be used two different ways: standalone and from within another script. The user will provide the title of the game, and the module will return a dictionary with the following details:

```json
{
    game_title: {
        'url': game_url, 
        'Main Story': main_hours, 
        'Main + Extra': extra_hours, 
        'Completionist': complete_hours
    }
}
```

For example, sending a query for `Final Fantasy` would return the following:
```json
{
    game_title: {
        'url': 'https://howlongtobeat.com/game.php?id=3480', 
        'Main Story': '17½Hrs', 
        'Main + Extra': '23½Hrs', 
        'Completionist': '35Hrs'
    }
}
```

#### Standalone
Run the following from the command line: `python3 scraper.py <game title>`
Example: `python3 scraper.py Final Fantasy`

#### Imported
* Import scraper.py into your file
* Use scraper.HLTB(game_title) to get game data
   * This will return the python dictionary detailed above

Example: `scraper.HLTB('Final Fantasy')`