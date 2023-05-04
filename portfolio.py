import dash_bootstrap_components as dbc
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State

app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ, "/Assets/estilos.css"])
server = app.server

navbar = dbc.NavbarSimple(
    children=[
       dbc.NavItem(dbc.NavLink("Home")),
       dbc.NavItem(dbc.NavLink("Sobre")),
       dbc.NavItem(dbc.NavLink("Portfólio")),
       dbc.NavItem(dbc.NavLink("Contato")) 
    ],
    brand="João Pedro",
    className='navbar-transparent',
    #color='#060606',
    dark=True,
    sticky='top',
    style={'borderBottom': 'none', 'height': '50px', 'navbar-transparent':'true'}, 
)

cover = html.Div([
    dbc.Row([
        dbc.Col([
            html.H5("Bem-Vindo(a), " ,style={'margin-left':'150px','margin right':'100px','text-align': 'justify'}),
            html.P("Meu nome é João Pedro do Carmo Costa Santos, sou Engenheiro de Produção, atualmente trabalhando como Analista de Custos e como Consultor de Business Intelligence.", style={"text-align": "justify", 'margin-left':'150px','margin right':'200px'}),
            html.P([
                dbc.Button('Veja meu Trabalho', outline=True, color="success", style={'margin-left':'150px'}),
            ], className="d-flex justify-content-justify")
        ], xs=12, sm=12, lg=8, md=8),
        dbc.Col([
            html.Img(src="https://media.licdn.com/dms/image/D4D03AQFP4olXaQdzGw/profile-displayphoto-shrink_800_800/0/1680175468993?e=1688601600&v=beta&t=oTIYwvFWVdYI1jS0TF41wwWJ1QKjduBVvgn6g3CA1L8",
                height=200,
                style={ "border-radius":"100px"})
        ], className="imagem-coluna", lg=4, md=4),
    ], style={'justify': 'center'}),
],  style={"width": "100%",
        "height": "50%",
        "padding": "10px",
        'margin-top': '25vh', 
        'margin-bottom': '25vh',
    }
)

CardCover1 = dbc.Card(
    dbc.CardBody([
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.H5(
                            "Bem-Vindo(a), ",
                            style={
                                #"margin-left": "50px",
                               # "margin-right": "100px",
                                "text-align": "justify",
                            },
                        ),
                        html.P(
                            "Meu nome é João Pedro do Carmo Costa Santos, sou Engenheiro de Produção, atualmente trabalhando como Analista de Custos e como Consultor de Business Intelligence.",
                            style={
                                "text-align": "justify",
                                #"margin-left": "50px",
                                #"margin-right": "200px",
                            },
                        ),
                        html.P(
                            [
                                dbc.Button(
                                    "Veja meu Trabalho",
                                    outline=True,
                                    color="success",
                                    #style={"margin-left": "50px"},
                                ),
                            ],
                            className="d-flex justify-content-justify",
                        ),
                    ],
                    xs=12,
                    sm=12,
                    lg=8,
                    md=8,
                    className="col-md-8",
                ),
                dbc.Col(
                    [
                        html.Img(
                            src="https://media.licdn.com/dms/image/D4D03AQFP4olXaQdzGw/profile-displayphoto-shrink_800_800/0/1680175468993?e=1688601600&v=beta&t=oTIYwvFWVdYI1jS0TF41wwWJ1QKjduBVvgn6g3CA1L8",
                            height=200,
                            #className="img-fluid",
                            style={"border-radius": "100%"},
                        )
                    ],
                    className="imagem-coluna",
                    lg=4,
                    md=4,
                ),
            ],
            #justify="center",
        )
    ], className='cardcover'),
    style={
      "margin-left": "5%",
       "margin-right": "5%",
       "margin-top": "25vh",
       "margin-bottom": "25vh",
        "background-color": "black",
    },
)

grid1 =html.Div([
    dbc.Row([
        html.H2(
            "Minha Formação", style={'margin-top':'50px',  'text-align':'center'}
        )
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("MBA em Engenharia de Negócios e Gestão de Empresas", className="card-title", style={'text-align':'center'}),
                    html.P("Baiana Business school (2022 - Atual)", className="card-title", style={'text-align':'center'}),
                    html.P("MBA em Gestão", style={'text-align':'center'})
                ])
            ], style={"background-color": "black", 'margin-left':'50px', 'margin-right':'50px', 'margin-botton':'25vh'})   
        ], xs=12, sm=12, lg=4, md=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Graduação em Engenharia de Produção", className="card-title", style={'text-align':'center'}),
                    html.P("Centro Universitário Senai Cimatec (2016 - 2021)", className="card-title", style={'text-align':'center'}),
                    html.P("Graduação em Engenharia", style={'text-align':'center'})
                ])
            ], style={"background-color": "black", 'margin-left':'50px', 'margin-right':'50px', 'margin-botton':'25vh'}) 
        ], xs=12, sm=12, lg=4, md=4) ,
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4("Graduação em Engenharia de Produção", className="card-title", style={'text-align':'center'}),
                    html.P("Centro Universitário Senai Cimatec (2016 - 2021)", className="card-title", style={'text-align':'center'}),
                    html.P("Graduação em Engenharia", style={'text-align':'center'})
                ])
            ], style={"background-color": "black", 'margin-left':'50px', 'margin-right':'50px', 'margin-botton':'25vh'})
        ], xs=12, sm=12, lg=4, md=4)
    ])
    ,html.Br()
])


footer = dbc.Container(    
    dbc.Row(
        dbc.Col(
            html.Div([
                html.P("Desenvolvido por João Pedro do Carmo, 2023 ", className="text-muted", style={"text-align": "center", "margin-top":"15px"}),
                html.A(html.Img(src=" https://cdn-icons-png.flaticon.com/512/3955/3955024.png ", height="30px", style={"margin-left": "10px"}), href="https://www.instagram.com/joaocarmo.co/", target="_blank"),
                html.A(html.Img(src="https://cdn-icons-png.flaticon.com/512/3955/3955051.png", height="30px",style={"margin-left": "10px"}), href="https://www.linkedin.com/in/joaodocarmo95/", target="_blank", className="ml-auto")
            ], className="d-flex align-items-center justify-content-center"),
            className="mt-2",
            style={"padding": "10px"}
        ),
    ),
    fluid=True,
    style={
        "position": "fixed",
        "bottom": "0",
        "width": "100%",  
        "color":"000000"          
    }
)  

app.layout = html.Div(
    [
        navbar,       
        CardCover1,  
        grid1,
        footer                      
    ], 
)


if __name__ == "__main__":
    app.run_server(port=8000, debug=True)