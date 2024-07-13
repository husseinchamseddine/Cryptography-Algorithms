from flask import Flask, request, jsonify,  render_template
from app import encrypt, decrypt  # Import your DES functions
import webbrowser
from threading import Timer
from AES import *
from playfair import *
from hillcipher import *
import ast 

app = Flask(__name__)

##################################################################

@app.route('/')
def home():
    return render_template('index.html')

##################################################################

@app.route('/DES/DES')
def des_page():
    return render_template('DES/DES.html')

@app.route('/DES/desDecryption')
def desDecryption_page():
    return render_template('DES/desDecryption.html')

@app.route('/DES/desEncryption')
def desEncryption_page():
    return render_template('DES/desEncryption.html')

##################################################################

@app.route('/AES/AES')
def aes_page():
    return render_template('AES/AES.html')

@app.route('/AES/aesEncryption')
def aesEncryption_page():
    return render_template('AES/aesEncryption.html')

@app.route('/AES/aesDecryption')
def aesDecryption_page():
    return render_template('AES/aesDecryption.html')

##################################################################

@app.route('/PF/PF')
def pf_page():
    return render_template('PF/PF.html')

@app.route('/PF/pfEncryption')
def pfEncryption_page():
    return render_template('PF/pfEncryption.html')

@app.route('/PF/pfDecryption')
def pfDecryption_page():
    return render_template('PF/pfDecryption.html')

##################################################################

@app.route('/HILL/HILL')
def hill_page():
    return render_template('HILL/HILL.html')

@app.route('/HILL/hillEncryption')
def hillEncryption_page():
    return render_template('HILL/hillEncryption.html')

@app.route('/HILL/hillDecryption')
def hillDecryption_page():
    return render_template('HILL/hillDecryption.html')

##################################################################

@app.route('/encrypt_hill', methods=['POST'])
def encrypt_hill():
    # Read key and text from form data
    key_string = request.form['key']
    text = request.form['text']

    # Convert the key from string format to a Python list of lists
    try:
        key = ast.literal_eval(key_string)
        assert len(key) == 2 and all(len(row) == 2 for row in key), "Key must be a 2x2 matrix."
    except (SyntaxError, ValueError, AssertionError) as e:
        return f"Invalid key format: {e}", 400

    # Create a cipher instance and encrypt the text
    cipher = HillCipher(key)
    encrypted_text = cipher.hill_cipher_2_enc(text)

    # Render a template with the encrypted text
    return render_template('HILL/hillEncryptionSolution.html', encrypted_text=encrypted_text)


##################################################################

@app.route('/decrypt_hill', methods=['POST'])
def decrypt_hill():
    # Read key and text from form data
    key_string = request.form['key']
    text = request.form['text']

    # Convert the key from string format to a Python list of lists
    try:
        key = ast.literal_eval(key_string)
        assert len(key) == 2 and all(len(row) == 2 for row in key), "Key must be a 2x2 matrix."
    except (SyntaxError, ValueError, AssertionError) as e:
        return f"Invalid key format: {e}", 400

    # Create a cipher instance and decrypt the text
    cipher = HillCipher(key)
    decrypted_text = cipher.hill_cipher_2_dec(text)

    # Render a template with the decrypted text
    return render_template('HILL/hillDecryptionSolution.html', decrypted_text=decrypted_text)

##################################################################

@app.route('/encrypt_pf', methods=['POST'])
def encrypt_pf():

    key1 = request.form['key1']
    key2 = request.form['key2']
    message = request.form['message']
    cipher = PlayfairCipher()
    matrix1 = cipher.create_matrix(key1)
    matrix2 = cipher.create_matrix(key2)
    encrypted_message = cipher.encrypt(message, matrix1, matrix2)
    return render_template('PF/pfEncryptionSolution.html', encrypted_message=encrypted_message)

##################################################################

@app.route('/decrypt_pf', methods=['POST'])
def decrypt_pf():

    key1 = request.form['key1']
    key2 = request.form['key2']
    message = request.form['message']
    cipher = PlayfairCipher()
    matrix1 = cipher.create_matrix(key1)
    matrix2 = cipher.create_matrix(key2)
    decrypted_message = cipher.decrypt(message, matrix1, matrix2)
    return render_template('PF/pfDecryptionSolution.html', decrypted_message=decrypted_message)

##################################################################

@app.route('/encrypt_des', methods=['POST'])
def encrypt_des():
    if request.method == 'POST':
        # Extract the message and key from the form data
        message = request.form['message']
        key = request.form['key']

        # Call the encrypt function from app.py
        encrypted_message, steps = encrypt(message, key)

        # Redirect to a new template that will show the encrypted message and steps
        return render_template('DES/desEncryptionSolution.html', encrypted_message=encrypted_message, steps=steps)

##################################################################

@app.route('/decrypt_des', methods=['POST'])
def decrypt_des():
    if request.method == 'POST':
        message = request.form['message']
        key = request.form['key']

        plaintext, steps = decrypt(message, key)

        # Pass the plaintext and steps to the template
        return render_template('DES/desDecryptionSolution.html', plaintext=plaintext, steps=steps)

##################################################################

@app.route('/encrypt_aes', methods=['POST'])
def encrypt_aes():
    if request.method == 'POST':
        # Extract the message and key from the form data
        message = request.form['message']
        key = request.form['key']

        # Call the encrypt function from app.py
        encrypted_message = AES(key,True,True).encrypt(message)
        # Redirect to a new template that will show the encrypted message and steps
        return render_template('AES/aesEncryptionSolution.html', encrypted_message=encrypted_message)

##################################################################

@app.route('/decrypt_aes', methods=['POST'])
def decrypt_aes():
    if request.method == 'POST':
        message = request.form['message']
        key = request.form['key']

        plaintext = AES(key,True,True).decrypt(message)

        # Pass the plaintext and steps to the template
        return render_template('AES/aesDecryptionSolution.html', plaintext=plaintext)
    
##################################################################

def open_browser():
      webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    Timer(1, open_browser).start()  # Wait 1 second before opening the web browser
    app.run(debug=True)


