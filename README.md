# JUDGE
#### **Bạn phải cài đặt python 3.9 trở lên để có thể sử dụng **
#### Cách sử dụng :
> python3 judge.py -h 

để biết thêm chi tiết

#### Lưu ý khi viết checker :
- Dữ liệu của file đầu vào của test sẽ nằm trong standar input 
- Tên file đầu ra sẽ nằm trong argv[1] của chương trình
- Tên file đáp án sẽ nằm trong argv[2] của chương trình
- Checker phải trả về 0 khi đúng, trả về 1 khi sai
- Các standar output của checker sẽ được hiện ra trong khi chấm

#### Lưu ý khi viết generator :
- Seed realtime sẽ nằm trong argv[1] để tránh việc random giống nhau