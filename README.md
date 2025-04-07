# Bazi-Calulate-All

## Run FastApi Local
```
uvicorn main_api:app --reload
```

## Docker

Build the image:
```
docker build -t fastapi-bazi-app .
```
Run the container with:
```
docker run -d -p 8003:8003 fastapi-bazi-app
```

## ตารางคำอธิบาย API - BaZi Calculator API

| API | Endpoint URL                    | Method | รายละเอียดการทำงาน                                                                 | ตัวอย่างการเรียกใช้                                                                 |
|--------|----------------------------------|--------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **API 1** | `/api/calculate_bazi`            | GET    | คำนวณเสาทั้ง 4 (ปี, เดือน, วัน, เวลา) พร้อมธาตุ, สิบเทพ (10 Gods), เสาโชค และสัดส่วนธาตุ | `/api/calculate_bazi?date_input=1990-01-01&time_input=13:00&sex=male`                |
| **API 2** | `/api/api2_current_energy`       | GET    | แสดงพลังธาตุของปีปัจจุบันและพลังของแต่ละเดือน (เสาปีและเสาเดือน)                     | `/api/api2_current_energy`                                                            |
| **API 3** | `/api/api3_five_year_forecast`   | GET    | ทำนายพลังธาตุรายปีล่วงหน้า 5 ปี (แสดงเฉพาะเสาปี)                                     | `/api/api3_five_year_forecast`                                                        |
| **API 4** | `/api/api4_next_week_energy`     | GET    | วิเคราะห์พลังธาตุของแต่ละวันใน "สัปดาห์หน้า" (พร้อมชื่อวัน เสาวัน เสาปี เสาเดือน)     | `/api/api4_next_week_energy`                                                          |

---

### หมายเหตุ:
- ทุก API ส่งคืนข้อมูลในรูปแบบ **JSON**
- หากไม่ใส่ `time_input` ใน API 1 ระบบจะตั้งค่าเวลาเริ่มต้นเป็น `12:00`
- ค่า `sex` ที่รองรับ: `male`, `female`
