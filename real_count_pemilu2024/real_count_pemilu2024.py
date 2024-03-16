import requests
from datetime import datetime
from config import Config

'''
don't delete this message.
created by ridwaanhall
'''

class DataFetcher:
    @staticmethod
    def get_data(url):
        try:
            response = requests.get(url, headers=Config.headers)
            response.raise_for_status()
            json_data = response.json()
            return json_data
        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None

class RealCountPemilu2024:
    def __init__(self):
        self.urls = {
            "ppwp": f"{Config.base_url}/pemilu/ppwp.json", # capres and cawapres
            "hhcw": f"{Config.base_url}/pemilu/hhcw/ppwp.json"
        }
        
    def get_data(self):
        ppwp_name = DataFetcher.get_data(self.urls["ppwp"])
        stat_reg = DataFetcher.get_data(self.urls["hhcw"])
        return ppwp_name, stat_reg

    def github_pages(self, output_file):
        ppwp_name, stat_reg = self.get_data()

        if ppwp_name is not None and stat_reg is not None:
            try:
                last_update = FormattedDate(stat_reg["ts"]).get_formatted_date()
            except ValueError:
                last_update = "Unknown"
            progress = stat_reg['progres']['progres']
            total_progress = stat_reg['progres']['total']
            percent = stat_reg['chart']['persen']

            percent_progress = progress / total_progress * 100

            total_votes = sum(stat_reg['chart'][key] for key in stat_reg['chart'] if key != 'persen')

            html_code_base = f'''
<!doctype html>
<html lang="en" data-bs-theme="dark">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Real Count Pemilu 2024</title>
        <meta name="description" content="Real Count - Pemilu 2024 data provided by Ridwaanhall">
        <meta name="keywords" content="Sirekap, Pemilu 2024, Real Count, Election, Indonesia, Ridwaanhall, {progress:>10,} of {total_progress:>10,} TPS, {last_update} | {percent_progress:.2f}%, {total_progress:>10,}">
        <meta name="author" content="Ridwan Halim">
        <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
        <meta name="revised" content="{last_update}">
        <meta name="language" content="English, Indonesian">
        <meta name="distribution" content="global">
        <meta name="rating" content="general">
        <meta http-equiv="X-UA-Compatible" content="IE=edge, chrome=1, safari=1, firefox=1, opera=1, edge=1, baidu=1, baiduspider=1">
        
        <meta name="referrer" content="no-referrer-when-downgrade">
        <meta name="format-detection" content="telephone=no">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black">
        <meta name="HandheldFriendly" content="True">
        <meta name="theme-color" content="#ffffff">
        <meta name="google" content="notranslate">
        
        <meta property="og:title" content="Ridwaanhall">
        <meta property="og:description" content="Real Count - Pemilu 2024 data provided by Ridwaanhall">
        <meta property="og:type" content="website">
        <meta property="og:url" content="https://ridwaanhall.github.io/pemilu2024.kpu.go.id/">
        <meta property="og:image:alt" content="Ridwaanhall Logo">
        <meta property="og:locale" content="en_US, id_ID">
        <meta name="twitter:card" content="">
        <meta name="twitter:title" content="Ridwaanhall, Real Count, Pemilu 2024, Indonesia, Prabowo Subianto, Anies Baswedan, Ganjar Pranowo">
        <meta name="twitter:description" content="Real Count - Pemilu 2024 data provided by Ridwaanhall">
        <meta name="twitter:url" content="https://ridwaanhall.github.io/pemilu2024.kpu.go.id/"> 

        <link rel="icon" type="image/x-icon" href="https://pemilu2024.kpu.go.id/favicon.ico">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    </head>
    <body style="padding-top: 70px">
        <nav class="navbar navbar-expand-lg bg-body-tertiary fixed-top">
            <div class="container">
                <a class="navbar-brand" href="https://ridwaanhall.github.io/pemilu2024.kpu.go.id/">
                    <img src="https://pemilu2024.kpu.go.id/assets/logo.7cbefe7d.png" alt="Logo" width="30" height="30" class="me-2">
                    <!--
                    <strong class="d-inline-block d-lg-none text-white">KPU</strong>
                    <strong class="d-none d-lg-inline-block text-white">General Election Commissions</strong>
                    -->
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarText">
                    <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                        <li class="nav-item">
                            <a class="nav-link" href="https://www.instagram.com/ridwaanhall">Instagram</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="https://www.linkedin.com/in/ridwaanhall">LinkedIn</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="https://github.com/ridwaanhall">Github</a>
                        </li>
                    </ul>
                    <span class="navbar-text badge text-bg-info d-none d-lg-inline-block">
'''
            last_update_content = f'''
                        Last update: {last_update}
                    </span>
                </div>
            </div>
        </nav>

        <div class="container">
            <h3 class="text-center mb-4">Real Count of Presidential and Vice Presidential Elections 2024</h3>
            <div class="alert alert-info alert-dismissible fade show" role="alert">
                <strong>Info!</strong> This data was 100% obtained from the <a href="https://pemilu2024.kpu.go.id/" class="alert-link">KPU</a>.
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
'''
            progress_content = f'''
            <div class="card mt-3">
                <div class="card-header">
                    REAL COUNT TABLE - PEMILU 2024
                    <div class="badge text-end text-bg-info d-inline-block d-lg-none">
                        Last update: {last_update}
                    </div>
                </div>
                <div class="card-body">
'''

            html_code_content = '''
                    <table class="table table-hover">
                        <thead>
                            <tr>
                                <th scope="col">#</th>
                                <th scope="col">PRESIDENTIAL CANDIDATE'S NAME</th>
                                <th scope="col">VICE PRESIDENTIAL CANDIDATE'S NAME</th>
                                <th scope="col">VOTES</th>
                                <th scope="col">PRECENT</th>
                            </tr>
                        </thead>
                        <tbody>
'''

            for key, value in ppwp_name.items():
                percent = stat_reg['chart'][key] / total_votes * 100
                name_parts = value['nama'].split(' - ')
                # print(name_parts)
                presidential = name_parts[0].strip()
                # print(presidential)# H. ANIES RASYID BASWEDAN, Ph.D.
                vice_presidential = name_parts[1].strip()
                # print(vice_presidential)
                html_code_content += f'''
                            <tr>
                                <td>{value['nomor_urut']:01d}</td>
                                <td>{presidential}</td>
                                <td>{vice_presidential}</td>
                                <td>{stat_reg['chart'][key]:,} of {total_votes:,}</td>
                                <td>{percent:.4f}%</td>
                            </tr>
'''

            html_code_content += '''
                        </tbody>
                    </table>
'''

            html_code_end = f'''
                </div>
                <div class="card-footer text-muted">
                    <blockquote class="blockquote mb-0 mt-3">
                        <footer class="blockquote-footer text-info">{progress:>10,} of {total_progress:>10,} TPS | <cite title="{percent_progress:.4f}%" class="badge text-bg-success">{percent_progress:.4f}% Done</cite></footer>
                    </blockquote>
                </div>
            </div>
            <div class="alert alert-danger mt-3 mb-4" role="alert">
                <h4 class="alert-heading">Attention!</h4>
                <p>This website has been created by <strong>Ridwan Halim (<em>ridwaanhall</em>)</strong> to provide information regarding the vote results for Presidential and Vice-Presidential Candidates, as The General Election Commissions (KPU) website does not display this information.</p>
                <hr>
                <p class="mb-0">Vote counting is carried out by KPPS, recapitulation of vote counting results and determination of election results are carried out in stages in open plenary meetings by PPK, Regency/City KPU, Provincial KPU and KPU based on the provisions of statutory regulations.</p>
            </div>
        </div>
        <!--
        <footer style="padding: 20px 0; text-align: center;">
            &copy; 2023 - Ridwaanhall
        </footer>
        -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
</html>
'''

            with open(output_file, 'w') as f:
                f.write(html_code_base)
                f.write(last_update_content)
                f.write(progress_content)
                f.write(html_code_content)
                f.write(html_code_end)
        else:
            print("Failed to fetch data from one of the URLs.")

class FormattedDate:
    def __init__(self, date_string):
        self.date_string = date_string

    def get_formatted_date(self):
        try:
            date_object = datetime.strptime(self.date_string, "%Y-%m-%d %H:%M:%S")
            formatted_date = date_object.strftime("%d %B %Y %H:%M:%S WIB")
            return formatted_date
        except ValueError:
            return "Invalid date format"

if __name__ == "__main__":
    pemilu_2024 = RealCountPemilu2024()
    pemilu_2024.github_pages('index.html')
