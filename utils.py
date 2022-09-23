import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import dcc
from dash import html


def print_percent(x):
    return f"{str(x * 100)[0:4]}%"


def find_img(champion, splashart=False):
    rename_champions = {
        "Xin Zhao": "XinZhao",
        "LeBlanc": "Leblanc",
        "Kog'Maw": "KogMaw",
        "Kha'Zix": "Khazix",
        "Jarvan IV": "JarvanIV",
        "Cho'Gath": "Chogath",
        "Aurelion Sol": "AurelionSol",
        "Tahm Kench": "TahmKench",
        "Rek'Sai": "RekSai",
        "Wukong": "MonkeyKing",
        "Miss Fortune": "MissFortune",
        "Master Yi": "MasterYi",
        "Lee Sin": "LeeSin",
        "Kai'Sa": "Kaisa",
        "Fiddlesticks": "FiddleSticks",
        "Dr. Mundo": "DrMundo",
        "Dr Mundo": "DrMundo",
        "Twisted Fate": "TwistedFate",
        "Vel'Koz": "Velkoz",
        "Renata Glasc": "Renata",
        "Nunu & Willump": "Nunu"
    }

    special_url = {
        'Akshan': 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/akshan/skins/base/akshanloadscreen.akshan.jpg',
        'Caitlyn': 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/caitlyn/skins/base/caitlynloadscreen_0.caitlyn_art_sustainability_update.jpg',
        'Dr. Mundo': 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/drmundo/skins/base/drmundoloadscreen_0.dr_mundo_vgu.jpg',
        'Gwen': 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/gwen/skins/base/gwenloadscreen_0.gwen.jpg',
        'Kassadin': 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/kassadin/skins/base/kassadinloadscreen_0.pie_c_12_6.jpg',
        'Vex': 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/vex/skins/base/vexloadscreen_0.s_yordle.jpg',
        'Viego': 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/viego/skins/base/viegoloadscreen.jpg',
        'Zeri': 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/zeri/skins/base/zeriloadscreen_0.zeri.jpg',
        'Renata Glasc': 'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/renata/skins/base/renataloadscreen_0.renata.jpg'}
    if champion in rename_champions.keys():
        champ = rename_champions[champion]
    else:
        champ = champion
    if not splashart:
        img_url = f'https://cdn.communitydragon.org/latest/champion/{champ}/square.png'

    else:
        if champion in special_url.keys():
            img_url = special_url[champion]
        elif str(champion) == 'None':
            champ = 'Teemo'
            img_url = f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/{champ.lower()}/skins/base/{champ.lower()}loadscreen.jpg"
        else:
            img_url = f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/assets/characters/{champ.lower()}/skins/base/{champ.lower()}loadscreen.jpg"

    return img_url


def draw_figure_player(position_data, role):
    kda = position_data[role]['kda']
    dpm = position_data[role]['dpm']
    dmgShare = position_data[role]['dmgShare']
    kp = position_data[role]['kp']
    goldShare = position_data[role]['goldShare']
    cspm = position_data[role]['cspm']
    soloKills = position_data[role]['soloKills']
    gd15 = position_data[role]['gd15']
    KDA15 = position_data[role]['KDA15']
    fwd = position_data[role]['fwd']
    fwdd = position_data[role]['fwdd']
    jp = position_data[role]['jp']
    jpd = position_data[role]['jpd']
    pinks15 = position_data[role]['pinks15']
    wards_cleared = position_data[role]['wards_cleared']
    pinks = position_data[role]['pinks']
    vspm = position_data[role]['VSPM']
    iso_deaths = position_data[role]['iso_deaths']
    soloKillsPost15 = position_data[role]['soloKillsPost15']
    efficiency = position_data[role]['efficiency']

    return html.Div([
        dbc.Card([
            html.Br(),
            html.H5("General"),
            html.Hr(),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([html.Div([html.H6("KDA")])]),
                    dbc.Col([html.Div([html.P(kda)])]),
                    dbc.Col([html.Div([html.H6("DPM")])]),
                    dbc.Col([html.Div([html.P(dpm)])]),

                ]),
                dbc.Row([
                    dbc.Col([html.Div([html.H6("DMG%")])]),
                    dbc.Col([html.Div([html.P(print_percent(dmgShare))])]),
                    dbc.Col([html.Div([html.H6("KP%")])]),
                    dbc.Col([html.Div([html.P(print_percent(kp))])]),

                ]),
                dbc.Row([
                    dbc.Col([html.Div([html.H6("Eff.")])]),
                    dbc.Col([html.Div([html.P(efficiency)])]),
                    dbc.Col([html.Div([html.H6("Gold%")])]),
                    dbc.Col([html.Div([html.P(print_percent(goldShare))])]),
                ]),
                dbc.Row([
                    dbc.Col([html.Div([html.H6("CSPM")])]),
                    dbc.Col([html.Div([html.P(cspm)])]),
                    dbc.Col([html.Div([html.H6("SoloKills")])]),
                    dbc.Col([html.Div([html.P(soloKills)])]),
                ])
            ]),
            html.H5("Early"),
            html.Hr(),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([html.Div([html.H6("GD@15")])]),
                    dbc.Col([html.Div([html.P(f"+{'%0.2f' %gd15}" if gd15 > 0 else f"{'%0.2f'% gd15}")])]),
                    dbc.Col([html.Div([html.H6("KDA@15")])]),
                    dbc.Col([html.Div(
                        [html.P(KDA15)])]),

                ]),
                dbc.Row([
                    dbc.Col([html.Div([html.H6("KP%@15")])]),
                    dbc.Col([html.Div([html.P(print_percent(fwd))])]),
                    dbc.Col([html.Div([html.H6("Enemy KP%@15")])]),
                    dbc.Col([html.Div([html.P(f"+{'%0.2f' %fwdd}" if fwdd > 0 else f"{'%0.2f' %fwdd}")])]),
                ]),
                dbc.Row([
                    dbc.Col([html.Div([html.H6("CS%")])]),
                    dbc.Col([html.Div([html.P(print_percent(jp))])]),
                    dbc.Col([html.Div([html.H6("CS-D%")])]),
                    dbc.Col([html.Div([html.P(f"+{'%0.2f' %jpd}" if jpd > 0 else f"{'%0.2f' %jpd}")])])]),
            ]),

            html.H5("Individuality"),
            html.Hr(),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([html.Div([html.H6("Pinks bought < @15")])]),
                    dbc.Col([html.Div([html.P(pinks15)])]),
                    dbc.Col([html.Div([html.H6("Wards Cleared")])]),
                    dbc.Col([html.Div([html.P(wards_cleared)])]),
                ]),
                dbc.Row([
                    dbc.Col([html.Div([html.H6("Pinks bought")])]),
                    dbc.Col([html.Div([html.P(pinks)])]),
                    dbc.Col([html.Div([html.H6("VSPM")])]),
                    dbc.Col([html.Div([html.P(vspm)])]),
                ]),
                dbc.Row([
                    dbc.Col([html.Div([html.H6("SoloDeaths")])]),
                    dbc.Col([html.Div([html.P(iso_deaths)])]),
                    dbc.Col([html.Div([html.H6("SoloKills > @15")])]),
                    dbc.Col([html.Div([html.P(soloKillsPost15)])]),
                ])
            ])
        ])
    ])


def draw_figure_champion_loss(team_data):
    champion_data_ = team_data['champion_data_loss']
    headers = dbc.ListGroupItem([
        dbc.Row([
            dbc.Col(html.Div(html.H6("Position"))),
            dbc.Col(html.Div(html.H6("Champion"))),
            dbc.Col(html.Div(html.H6("Games"))),
            dbc.Col(html.Div(html.H6("Your Efficiency"))),
        ])
    ])
    divs_champs = [headers]
    for k in champion_data_:
        role = k[0]
        champ = k[1]
        gp = k[2]
        winrate_ = k[3]
        chp_gd15_ = k[4]
        winrate = float(winrate_)
        chp_gd15 = float(chp_gd15_)

        if winrate >= 0.80:
            color1 = "red"
        elif (winrate < 0.80) and (winrate >= 0.55):
            color1 = "lightsalmon"
        elif (winrate < 0.55) and (winrate >= 0.45):
            color1 = "grey"
        elif (winrate < 0.45):
            color1 = "green"

        if chp_gd15 >= 450:
            color2 = "red"
        elif (chp_gd15 < 450) and (chp_gd15 >= 150):
            color2 = "lightred"
        elif (chp_gd15 < 150) and (chp_gd15 >= -200):
            color2 = "lightgrey"
        elif (chp_gd15 < -200):
            color2 = "green "

        if winrate <= 0.25:
            progress_bar = dbc.Col(
                html.Div(dbc.Progress(label=str(int(100 * winrate)) + '%', value=100 * 0.3, color=color1,
                                      className='mb-3')), width=3)
        else:
            progress_bar = dbc.Col(
                html.Div(dbc.Progress(label=str(int(100 * winrate)) + '%', value=100 * winrate, color=color1,
                                      className='mb-3')), width=3)

        champ_line = dbc.ListGroupItem([
            dbc.Row([
                dbc.Col(html.Div(html.P(role))),
                dbc.Col(html.Div(html.Img(src=find_img(champ), height="27px"))),
                dbc.Col(html.Div(html.P(int(float(gp))))),
                progress_bar,
                # dbc.Col(html.Div(html.P(print_percent(winrate), style={'font-weight': 'bold', 'color': color}))),
            ], justify="center", align="center", className="h-50")
        ])
        divs_champs.append(champ_line)

    return html.Div([
        dbc.ListGroup(
            divs_champs
        )
    ])


def draw_figure_champion(champion_data, role="Top"):
    print(champion_data)
    headers = dbc.ListGroupItem([
        dbc.Row([
            dbc.Col(html.Div(html.H6("Champion", style={'font-size': '0.6em'}))),
            dbc.Col(html.Div(html.H6("Games", style={'font-size': '0.6em'}))),
            dbc.Col(html.Div(html.H6("Winrate", style={'font-size': '0.6em'}))),
            dbc.Col(html.Div(html.H6("GD@15", style={'font-size': '0.6em'})))
        ])
    ])
    divs_champs = [headers]
    for k in champion_data[role]:
        champ = k[0]
        gp = k[1]
        winrate_ = k[2]
        chp_gd15_ = k[3]
        winrate = float(winrate_)
        chp_gd15 = float(chp_gd15_)

        if winrate > 0.80:
            color1 = "green"
        elif (winrate < 0.80) and (winrate >= 0.55):
            color1 = "#90EE90"
        elif (winrate < 0.55) and (winrate >= 0.45):
            color1 = "grey"
        elif (winrate < 0.45) and (winrate >= 0.3):
            color1 = "lightsalmon"
        elif (winrate < 0.3):
            color1 = "red"

        if chp_gd15 > 450:
            color2 = "green"
        elif (chp_gd15 < 450) and (chp_gd15 > 150):
            color2 = "#90EE90"
        elif (chp_gd15 < 150) and (chp_gd15 > -200):
            color2 = "grey"
        elif (chp_gd15 < -200):
            color2 = "red"

        if winrate <= 0.29:
            progress_bar = dbc.Col(
                html.Div(dbc.Progress(label=str(int(100 * winrate)) + '%', value=100 * 0.35, color=color1,
                                      className='mb-3', style={'font-size': '0.65em'})), width=3)
        else:
            progress_bar = dbc.Col(
                html.Div(dbc.Progress(label=str(int(100 * winrate)) + '%', value=100 * winrate, color=color1,
                                      className='mb-3', style={'font-size': '0.65em'})), width=3)

        champ_line = dbc.ListGroupItem([
            dbc.Row([
                dbc.Col(html.Div(html.Img(src=find_img(champ), height="27px"))),
                dbc.Col(html.Div(html.P(int(float(gp))))),
                progress_bar,
                dbc.Col(html.Div(html.P(f"+{'%0.2f' % chp_gd15}" if chp_gd15 > 0 else f"{'%0.2f' % chp_gd15}",
                                        style={'font-weight': 'bold', 'color': color2})))

            ], justify="center", align="center", className="h-50")
        ])

        divs_champs.append(champ_line)

    return html.Div([
        dbc.ListGroup(
            divs_champs
        )
    ])


def draw_figure_team(team_data):
    games = team_data['games']
    gameduration = team_data['gameduration']
    kills = team_data['kills']
    deaths = team_data['deaths']
    kd = team_data['kd']
    gdm = team_data['gdm']
    teamgd15 = team_data['teamgd15']
    kd15 = team_data['kd15']
    first_rift = team_data['firstRift']
    first_dragon = team_data['firstDragon']
    dragonKills = team_data['dragonKills']
    dragonShare = team_data['dragonShare']
    riftHeraldKills = team_data['riftHeraldKills']
    riftShare = team_data['riftShare']
    dragons15 = team_data['dragons15'],
    timerNash = team_data['timerNash']

    team_data_sides = team_data['sides']
    blue_side_data = pd.DataFrame([['Win', team_data_sides['Blue'][0]], ['Loss', team_data_sides['Blue'][1]]],
                                  columns=['Win or Lose', 'Number of Games'])

    red_side_data = pd.DataFrame([['Win', team_data_sides['Red'][0]], ['Loss', team_data_sides['Red'][1]]],
                                 columns=['Win or Lose', 'Number of Games'])

    total_wr = (team_data_sides['Blue'][0] + team_data_sides['Red'][0]) / (
            team_data_sides['Blue'][0] + team_data_sides['Red'][0] + team_data_sides['Blue'][1] +
            team_data_sides['Red'][1])

    fig_blue = px.pie(
        blue_side_data,
        values="Number of Games",
        names="Win or Lose",
        color="Win or Lose",
        title="Blue W/R",
        color_discrete_map={
            "Win": "royalblue",
            "Loss": "darkblue",
        },
    )

    fig_blue.update_traces(hoverinfo='label+percent', textfont_size=20,
                           marker=dict(line=dict(color='#000000', width=2)))

    red_colors = ['darkorange', 'gold']
    fig_red = px.pie(
        red_side_data,
        values="Number of Games",
        names="Win or Lose",
        title="Red W/R",
    )

    fig_red.update_traces(hoverinfo='label+percent', textfont_size=20,
                          marker=dict(colors=red_colors, line=dict(color='#000000', width=2)))

    fig_wr = go.Figure()
    fig_wr.add_trace(go.Indicator(
        mode="number",
        value=total_wr,
        number={'valueformat': '.0%'},
        title={'text': 'Total Winrate'}
    ))

    return html.Div([
        dbc.Card(

            dbc.CardBody([
                html.H4("W/R Distribution"),
                html.Hr(),
                dbc.Row([
                    dbc.Col([dcc.Graph(
                        figure=fig_wr, style={'width': '25vh', 'height': '25vh'}
                    )]),
                    dbc.Col([dcc.Graph(
                        figure=fig_blue, style={'width': '25vh', 'height': '25vh'}
                    )]),
                    dbc.Col([dcc.Graph(
                        figure=fig_red, style={'width': '25vh', 'height': '25vh'}
                    )])
                ]),

                html.H4("General Stats"),
                html.Hr(),
                dbc.Row([
                    dbc.Col([html.Div([html.H6("Number of Games")])]),
                    dbc.Col([html.Div([html.P(games)])]),
                    dbc.Col([html.Div([html.H6("Game Duration")])]),
                    dbc.Col([html.Div([html.P(gameduration)])]),
                    dbc.Col([html.Div([html.H6("Kills/Deaths")])]),
                    dbc.Col([html.Div([html.P(f"{kills}/{deaths} ({str(kd)[0:4]})")])]),
                    dbc.Col([html.Div([html.H6("GD/M")])]),
                    dbc.Col([html.Div([html.P(f"+{'%0.2f' % gdm}" if gdm > 0 else f"{'%0.2f' %gdm}")])]),
                ]),
                dbc.Row([
                    dbc.Col([html.Div([html.H6("GD@15")])]),
                    dbc.Col([html.Div([html.P(f"+{'%0.2f' % teamgd15}" if teamgd15 > 0 else f"{'%0.2f' %teamgd15}")])]),
                    dbc.Col([html.Div([html.H6("KD@15")])]),
                    dbc.Col([html.Div([html.P(kd15)])]),
                    dbc.Col([html.Div([html.H6("FirstRift%")])]),
                    dbc.Col([html.Div([html.P(print_percent(first_rift))])]),
                    dbc.Col([html.Div([html.H6("FirstDragon%")])]),
                    dbc.Col([html.Div([html.P(print_percent(first_dragon))])]),

                ]),
                dbc.Row([
                    dbc.Col([html.Div([html.H6("Dragons/Game")])]),
                    dbc.Col([html.Div([html.P(f"{dragonKills} ({print_percent(dragonShare)})")])]),
                    dbc.Col([html.Div([html.H6("Rifts/Games")])]),
                    dbc.Col([html.Div([html.P(f"{riftHeraldKills} ({print_percent(riftShare)})")])]),
                    dbc.Col([html.Div([html.H6("Dragons@15")])]),
                    dbc.Col([html.Div([html.P(dragons15)])]),
                    dbc.Col([html.Div([html.H6("Timer 1st Nashor")])]),
                    dbc.Col([html.Div([html.P(timerNash)])]),
                ])

            ])
        ),
    ])


# Text field
def drawText(text):
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2(text),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])

def create_analytic_content(team_data, position_data, champion_data):
    top_name = position_data['Top']['name']
    jungle_name = position_data['Jungle']['name']
    mid_name = position_data['Mid']['name']
    adc_name = position_data['ADC']['name']
    support_name = position_data['Support']['name']
    champion_data_loss = team_data['champion_data_loss']

    return dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawText("What does your team do ?")
                ], width=8),
                dbc.Col([
                    drawText("Your most effective champions")
                ], width=3),
            ], align='center', justify="center"),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    draw_figure_team(team_data)
                ], width=8),
                dbc.Col([
                    draw_figure_champion_loss(team_data)
                ], width=3),
            ], align='center', justify="center"),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawText(top_name)
                ], width=2),
                dbc.Col([
                    drawText(jungle_name)
                ], width=2),
                dbc.Col([
                    drawText(mid_name)
                ], width=2),
                dbc.Col([
                    drawText(adc_name)
                ], width=2),
                dbc.Col([
                    drawText(support_name)
                ], width=2)
            ], align='center', justify="center"),
            html.Br(),

            dbc.Row([
                dbc.Col([
                    draw_figure_player(position_data, role="Top")
                ], width=2),
                dbc.Col([
                    draw_figure_player(position_data, role="Jungle")
                ], width=2),
                dbc.Col([
                    draw_figure_player(position_data, role="Mid")
                ], width=2),
                dbc.Col([
                    draw_figure_player(position_data, role="ADC")
                ], width=2),
                dbc.Col([
                    draw_figure_player(position_data, role="Support")
                ], width=2),
            ], align='center', justify='center'),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    draw_figure_champion(position_data['Top']['champion_data'], role="Top")
                ], width=2, ),
                dbc.Col([
                    draw_figure_champion(position_data['Jungle']['champion_data'], role="Jungle")
                ], width=2, ),
                dbc.Col([
                    draw_figure_champion(position_data['Mid']['champion_data'], role="Mid")
                ], width=2, ),
                dbc.Col([
                    draw_figure_champion(position_data['ADC']['champion_data'], role="ADC")
                ], width=2, ),
                dbc.Col([
                    draw_figure_champion(position_data['Support']['champion_data'], role="Support")
                ], width=2, ),
            ], align='center', justify='center')

        ]), color='dark',
    )
# ----------------
