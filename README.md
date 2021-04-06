# HandGestureClassifier
Hand gesture classifier using Support Vector Machine with sEMG Signal.
Figure out the effect of PCA, LDA and SVD on feature decomposition of sEMG signal classification for hand motion detection using the SVM algorithm.

The features used in this research:
1. RMS
2. MAV
3. SAV
4. WL
5. HP
6. STD

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
