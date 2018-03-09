
# Train it
python -m rasa_nlu.train -c config_mitie.json

# Host it
python -m rasa_nlu.server -c config_mitie.json

# Ok I am writing this only coz  I know I will forget
curl -X POST localhost:5001/parse -d '{"q":"Ok Bye"}' | python -m json.tool

