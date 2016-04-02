
@todo : Document example cURL calls to the OAuth2 Authentication Server

### Resource Owner Password

curl -X POST -d "grant_type=password&username=mark&password=P@55w0rd" http://localhost:8000/o/token


curl -X POST -d "client_id=jWFRwqFLDGvgWn6Fd1mt6ynClcDLkltLxvZFXa4x&amp;client_secret=b6PNTFh7MDys6deI8Rcw3WK3s6t5h7bpqIAQY7VNfboNm1l6CD9Jj9NEP3BD893fsLXbADjyhuvEgNj6UeC2TaWEujCvgHoXCzaam5lHuN5QK9mTLwARgFKsD4YzIei2&amp;grant_type=password&amp;username=mark&amp;password=P@55w0rd" http://localhost:8000/o/token