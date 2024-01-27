import cv2
import tkinter as tk
from tkinter import Scale
from PIL import Image, ImageTk
import numpy as np

class ImageEnhancerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Enhancer App")

        # Load gambar dari file
        self.original_img = cv2.imread("images/naruto.jpg")

        # Nilai awal untuk kontrol pengaturan
        self.contrast_value = tk.DoubleVar()
        self.contrast_value.set(1.5)  # Nilai kontras awal

        self.brightness_value = tk.DoubleVar()
        self.brightness_value.set(10)  # Nilai kecerahan awal

        self.saturation_value = tk.DoubleVar()
        self.saturation_value.set(1.5)  # Nilai saturasi awal

        # Tampilkan gambar asli
        self.display_original_image()

        # Kontrol pengaturan
        self.create_controls()

        # Tombol untuk memperindah gambar
        enhance_button = tk.Button(self.master, text="Enhance Image", command=self.enhance_image)
        enhance_button.grid(row=1, column=0, pady=10)

    def display_original_image(self):
        # Resize gambar agar sesuai dengan jendela
        resized_img = cv2.resize(self.original_img, (400, 300))

        # Konversi gambar OpenCV ke format PIL
        original_img_pil = Image.fromarray(cv2.cvtColor(resized_img, cv2.COLOR_BGR2RGB))

        # Konversi gambar PIL ke format PhotoImage Tkinter
        original_img_tk = ImageTk.PhotoImage(original_img_pil)

        # Tampilkan gambar dalam label Tkinter
        label = tk.Label(self.master, image=original_img_tk)
        label.image = original_img_tk  # Jaga referensi agar tidak dihapus oleh garbage collector
        label.grid(row=3, column=0, columnspan=2, pady=10)

    def create_controls(self):
        # Kontrol pengaturan kontras
        contrast_label = tk.Label(self.master, text="Contrast:")
        contrast_label.grid(row=2, column=0)
        contrast_slider = Scale(self.master, from_=1, to=3, resolution=0.1, variable=self.contrast_value, orient=tk.HORIZONTAL)
        contrast_slider.grid(row=2, column=1)

        # Kontrol pengaturan kecerahan
        brightness_label = tk.Label(self.master, text="Brightness:")
        brightness_label.grid(row=2, column=2)
        brightness_slider = Scale(self.master, from_=-50, to=50, resolution=1, variable=self.brightness_value, orient=tk.HORIZONTAL)
        brightness_slider.grid(row=2, column=3)

        # Kontrol pengaturan saturasi
        saturation_label = tk.Label(self.master, text="Saturation:")
        saturation_label.grid(row=2, column=4)
        saturation_slider = Scale(self.master, from_=0.1, to=3, resolution=0.1, variable=self.saturation_value, orient=tk.HORIZONTAL)
        saturation_slider.grid(row=2, column=5)

    def enhance_image(self):
        # Mendapatkan nilai dari kontrol pengaturan
        contrast_factor = self.contrast_value.get()
        brightness_factor = self.brightness_value.get()
        saturation_factor = self.saturation_value.get()

        # Implementasikan peningkatan gambar di sini
        enhanced_img = self.adjust_image(self.original_img, contrast_factor, brightness_factor, saturation_factor)

        # Resize gambar hasil agar sesuai dengan jendela
        resized_enhanced_img = cv2.resize(enhanced_img, (400, 300))

        # Konversi gambar OpenCV ke format PIL
        enhanced_img_pil = Image.fromarray(cv2.cvtColor(resized_enhanced_img, cv2.COLOR_BGR2RGB))

        # Konversi gambar PIL ke format PhotoImage Tkinter
        enhanced_img_tk = ImageTk.PhotoImage(enhanced_img_pil)

        # Tampilkan gambar hasil peningkatan dalam label Tkinter
        enhanced_label = tk.Label(self.master, image=enhanced_img_tk)
        enhanced_label.image = enhanced_img_tk  # Jaga referensi agar tidak dihapus oleh garbage collector
        enhanced_label.grid(row=3, column=3, columnspan=2, pady=10)

    def adjust_image(self, img, contrast_factor, brightness_factor, saturation_factor):
        # Contoh: Peningkatan kontras, kecerahan, dan saturasi
        enhanced_img = cv2.convertScaleAbs(img, alpha=contrast_factor, beta=brightness_factor)

        # Konversi warna dari BGR ke HSV
        hsv = cv2.cvtColor(enhanced_img, cv2.COLOR_BGR2HSV)

        # Mengatur nilai saturasi
        hsv[:,:,1] = np.clip(hsv[:,:,1] * saturation_factor, 0, 255)

        # Konversi kembali dari HSV ke BGR
        enhanced_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        return enhanced_img

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageEnhancerApp(root)
    root.mainloop()
