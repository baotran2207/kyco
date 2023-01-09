import gspread

gc_credentials_filename = "/Users/baotran/.config/gspread/credentials.json"
gc_authorized_user_filename = "/Users/baotran/.config/gspread/credentials.json"

gc = gspread.oauth(
    credentials_filename=gc_credentials_filename,
    authorized_user_filename=gc_authorized_user_filename,
)
