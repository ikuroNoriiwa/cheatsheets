# Debug Python 


## Debug using VSCODE Integrated option 
Init debug server : 
```
python -m debugpy --listen 0.0.0.0:5678 ./main.py 
```

Create config file in debug mode VSCode 
```
{
    "version": "0.2.0",
    "configurations": [      
        {
            "name": "Attach",
            "type": "python",
            "request": "attach",
            "connect": {
                "host": "127.0.0.1",
                "port": 5678
            },
            "justMyCode": true
        }
    ]
}
```