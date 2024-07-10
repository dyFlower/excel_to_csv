import pandas as pd

excel_file_path = 'ExcelData/일탈.xlsx'
save_file_name = excel_file_path.split('/')[-1].split('.')[0]

# 엑셀 파일 읽기
df = pd.read_excel(excel_file_path, header=None)

# 범위 값 추출
storage_temp_range = df.loc[6, 3]
min_temp, max_temp = map(float, storage_temp_range.replace("℃", "").split(" ~ "))

# 필요한 데이터 추출
data = df.iloc[10:, [1, 2, 3, 4]]
data.columns = ["idx", "temperature(℃)", "humidity(%)", "timestamp"]

# 각 열에 데이터 추가
data["min_temp"] = min_temp
data["max_temp"] = max_temp

# 열 순서를 조정
final_data = data[["timestamp", "temperature(℃)", "humidity(%)", "min_temp", "max_temp"]]

# CSV 파일 저장
csv_file_path = f'csvData/{save_file_name}.csv'
final_data.to_csv(csv_file_path, index=False)

print(f"CSV 파일이 생성되었습니다: {csv_file_path}")