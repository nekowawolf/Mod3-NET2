import tkinter as tk
import socket


class NslookupApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Nslookup App")

        # Buat label dan entri untuk domain
        self.domain_label = tk.Label(master, text="Masukan Domain:")
        self.domain_label.pack(pady=10)
        self.domain_entry = tk.Entry(master)
        self.domain_entry.pack()

        # Buat tombol untuk menjalankan fungsi nslookup()
        self.lookup_button = tk.Button(master, text="Nslookup", command=self.nslookup)
        self.lookup_button.pack(pady=10)

        # Buat label untuk menampilkan hasil nslookup
        self.result_label = tk.Label(master, text="", wraplength=300)
        self.result_label.pack()

    def nslookup(self):
        domain_to_lookup = self.domain_entry.get()

        try:
            # Lakukan nslookup domain
            result = socket.gethostbyname(domain_to_lookup)

            # Tampilkan hasil nslookup
            self.result_label.config(text=f"Hasil nslookup {domain_to_lookup}: {result}")
        except socket.error:
            # Tangani kesalahan nslookup
            self.result_label.config(text="Gagal melakukan nslookup domain")


if __name__ == '__main__':
    root = tk.Tk()

    app = NslookupApp(root)
    root.mainloop()
