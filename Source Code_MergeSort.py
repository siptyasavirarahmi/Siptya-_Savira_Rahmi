# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
  
         # Menemukan bagian tengah array
        mid = len(arr)//2
  
        # Membagi elemen array
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Menyortir paruh pertama
        mergeSort(L)
  
        # Menyortir paruh kedua
        mergeSort(R)
  
        i = j = k = 0
  
        # Salin data ke temp arrays L[] dan R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Memeriksa apakah ada elemen yang tersisa
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
  
# Kode untuk mencetak daftar
  
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
  
  
# Kode Pengemudi
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is", end="\n")
    printList(arr)
    mergeSort(arr)
    print("Sorted array is: ", end="\n")
    printList(arr)
  