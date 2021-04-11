# HandGestureClassifier
Hand gesture classifier using Support Vector Machine with sEMG Signal.
Mencari tahu pengaruh dari penggunaan PCA, LDA, SVD pada pengklasifikasian gerakan tangan menggunakan data sEMG.
Dataset yang digunakan dapat diakses melalui:
https://archive.ics.uci.edu/ml/datasets/EMG+data+for+gestures


Penjelasan Lebih lanjut untuk masing-masing file program:
**#preprocess.py**
Untuk melakukan tahap preprocessing yang diinginkan.

**#ft.py**
merupakan program untuk melakukan ekstraksi fitur sesuai fitur yang sudah ditentukan diatas. Fitur yang diekstraksi dapat kita pilih. Contoh: hanya ingin menggunakan 3 fitur saja. Hal tersebut dapat dilakukan untuk penjelas lebih jauh dapat dilihat didalam file **ft.py** secara langsung

**#extract.py**
file utama untuk membentuk dataset baru dari dataset sebelumnya yang berisi data mentah. Sedangkan dengan menggunakan program ini dapat membuat dataset baru yang berisi fitur-fitur yang akan diekstrak menggunakan program dari **#preprocess.py** dan **#ft.py**

**#classification.py**
Program untuk memulai pemodelan klasifikasi menggunakan metode SVM, dimana hasil pemodelan dapat disimpan dalam format SAV

**#LDA_.py**
program untuk membuat pemodelan menggunakan LDA decomposition pada fitur ekstraksi

**#PCA_.py**
program untuk membuat pemodelan menggunakan PCA decomposition pada fitur ekstraksi

**#Folder MODEL**
folder ini berisi model machine learning SVM yang bisa digunakan untuk langsung memprediksi gerakan tangan. Didalam folder tersebut sudah lengkap dengan metode dekomposisi apa yang digunakan dan berapa banyak komponen yang digunakan. Untuk SVD dan PCA digunakan komponen sebanyak 2,4,8,16 dan 32 komponen. Sedangkan untuk LDA menggunakan 1,2,3,4 dan 5 komponen
