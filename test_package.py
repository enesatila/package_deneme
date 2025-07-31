def test_connection():
    import sys
    from datetime import datetime
    
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = {
            "status": "SUCCESS",
            "message": "Kütüphane başarıyla çalışıyor!",
            "python_version": sys.version,
            "test_time": current_time,
            "test_passed": True
        }
        print(f"✅ Test başarılı - {current_time}")
        return result
    except Exception as e:
        print(f"❌ Test başarısız: {e}")
        return {"status": "ERROR", "error": str(e)}
