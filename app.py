# import library 
from urllib import response
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# Inisiasi Object
app = Flask(__name__)

# Inisiasi object flask_restful
api = Api(app)

# Inisiasi dari Flask Cors
CORS(app)

# Inialisasi variabel bertipe dictionary
identitas = {}

# Membuat class Resource
class ContohResource(Resource):
    # method GET
    def get(self):
        #response = {"msg": "Halo ini dari Flask Rest API"}
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg": "Data berhasil dimasukkan"}
        return response

#setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)

