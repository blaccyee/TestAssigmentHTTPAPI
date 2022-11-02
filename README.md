# TestAssigmentHTTPAPI
 
I'm really sorry, I didn't manage to create a proper docker-compose.yml file. I just stuck on connection error "This site can't be reached" when a container is running. 

But it can be tested anyway!

### *Here is a little instruction*

0) Open PyCharm (or something else)
1) In Terminal execute 'pip install -e .'
2) To run a server execute 'uvicorn app.main:app'
3) Follow the link http://127.0.0.1:8000/docs (API documentation)

*If you've got different host and port just click it in your terminal and add '/docs' at the end of the address*
![image](https://user-images.githubusercontent.com/24205756/199099294-6bfef99f-d639-48d1-9c8f-30e58d4814b0.png)

4) To check the documentation click on any method you want
![image](https://user-images.githubusercontent.com/24205756/199100162-bc64ebd4-38c8-4b78-a946-dc4f13f96fab.png)

5) To run any method click on "Try it out" button
![image](https://user-images.githubusercontent.com/24205756/199100310-4ba508e5-5dba-4a3b-b3d9-9816791b3d77.png)
- fill a request body if needed
- click on "Execute" button

6) To finish a work of server go to your terminal and type Ctrl+C

I hope you find it helpful.
