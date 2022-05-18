# Forms and File Uploads Verification with FastAPI.

    
## Getting started

Create a virtual environment for the project:  
`python3 -m venv virtualenv`

Then activate the virtual environment:  
`source virtualenv/bin/activate`  
Or on Powershell:  
`.\virtualenv\Scripts\Activate.ps1`

Now install the dependencies for the project:  
`pip install -r requirements.txt`

You should now be able to run the API with:  
`uvicorn app:app`

To Test with cURL:

    curl --location --request POST 'http://127.0.0.1:8000/ --form 'partner_key=""' --form 'secret_key=""' --form 'tags=""' --form 'first_name=""' --form 'last_name=""' --form 'email=""' --form 'resume_file=@"/path/to/file"'

