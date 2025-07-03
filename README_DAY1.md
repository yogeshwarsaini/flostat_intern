# ✅ Day 1 – Flostat Internship

## 🔹 Lambda Function 1 (Hello World)
- **Name:** helloworld_yogeshwar
- **API Gateway URL:** https://xyz123.execute-api.ap-south-1.amazonaws.com/hello
- **Response:** {"message": "Hello from Yogeshwar!"}

## 🔹 DynamoDB + Lambda Function
- **Lambda Name:** datahandler_yogeshwar
- **DynamoDB Table:** tank-updates-yogeshwar
- **GET URL Example:** https://xyz123.execute-api.ap-south-1.amazonaws.com/save?device_id=007&name=yogi
- **Functionality:**
  - Takes `device_id` and `name` as query parameters
  - Inserts into DynamoDB
  - Fetches and returns latest value

## 📸 CloudWatch Logs
(Screenshot attached below)

![cloudwatch_1](https://github.com/user-attachments/assets/493121f2-01ce-44dd-9ee6-7d3c3b30ec6c)


## ✅ Summary:
- Created Hello World Lambda
- Connected Lambda to API Gateway
- Inserted & fetched data from DynamoDB table: `tank-updates-yogeshwar`
- Logs verified on CloudWatch

## 🔗 GitHub Link:
https://github.com/YOUR-USERNAME/AWS_Interns/tree/main/Yogeshwar
