from currencycat import app
app.run(port=environ.get("PORT", 5000), debug=True)
