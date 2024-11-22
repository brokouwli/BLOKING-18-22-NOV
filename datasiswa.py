import PySimpleGUI as sg

# Define the layout of the form
layout = [
    # Header with blue background
    [sg.Text("Data Siswa Baru", size=(30, 1), justification='center', font=("Helvetica", 16), text_color="white", background_color="blue")],
    
    # Input fields
    [sg.Text("Nama Lengkap:", size=(15, 1)), sg.InputText(key='NAMA_LENGKAP')],
    [sg.Text("Tanggal Lahir (dd-mm-yyyy):", size=(15, 1)), sg.InputText(key='TANGGAL_LAHIR')],
    [sg.Text("Asal Sekolah:", size=(15, 1)), sg.InputText(key='ASAL_SEKOLAH')],
    [sg.Text("NISN:", size=(15, 1)), sg.InputText(key='NISN')],
    [sg.Text("Nama Ayah:", size=(15, 1)), sg.InputText(key='NAMA_AYAH')],
    [sg.Text("Nama Ibu:", size=(15, 1)), sg.InputText(key='NAMA_IBU')],
    [sg.Text("Nomor Telepon/HP:", size=(15, 1)), sg.InputText(key='NOMOR_TELEPON')],
    [sg.Text("Alamat:", size=(15, 1)), sg.Multiline(size=(40, 3), key='ALAMAT')],
    
    # Buttons
    [sg.Button("Simpan"), sg.Button("Hapus"), sg.Exit()]
]

# Create the window
window = sg.Window(
    "Program Data Siswa",
    layout,
    element_justification='left',  # Standard alignment for input form
    background_color="white",  # Set background color for the entire window
)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Simpan":
        # Collect input data
        data_siswa = {
            "Nama Lengkap": values['NAMA_LENGKAP'],
            "Tanggal Lahir": values['TANGGAL_LAHIR'],
            "Asal Sekolah": values['ASAL_SEKOLAH'],
            "NISN": values['NISN'],
            "Nama Ayah": values['NAMA_AYAH'],
            "Nama Ibu": values['NAMA_IBU'],
            "Nomor Telepon/HP": values['NOMOR_TELEPON'],
            "Alamat": values['ALAMAT']
        }
        
        # Save data or display confirmation
        sg.popup("Data Tersimpan", "Berikut data yang Anda masukkan:", "\n".join(f"{k}: {v}" for k, v in data_siswa.items()))
    
    elif event == "Hapus":
        # Clear all input fields
        for key in values.keys():
            window[key]('')
        sg.popup("Form telah dihapus!")

# Close the window
window.close()