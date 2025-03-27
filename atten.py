from datetime import datetime, timedelta
from collections import defaultdict


attendance_data = [
    {'student_id': 101, 'attendance_date': '2024-03-01', 'status': 'Absent'},
    {'student_id': 101, 'attendance_date': '2024-03-02', 'status': 'Absent'},
    {'student_id': 101, 'attendance_date': '2024-03-03', 'status': 'Absent'},
    {'student_id': 101, 'attendance_date': '2024-03-04', 'status': 'Absent'},
    {'student_id': 101, 'attendance_date': '2024-03-05 'status': 'Present'},
    {'student_id': 102, 'attendance_date': '2024-03-02', 'status': 'Absent'},
    {'student_id': 102, 'attendance_date': '2024-03-03', 'status': 'Absent'},
    {'student_id': 102, 'attendance_date': '2024-03-04', 'status': 'Absent'},
    {'student_id': 103, 'attendance_date': '2024-03-05', 'status': 'Absent'},
    {'student_id': 103, 'attendance_date': '2024-03-05', 'status': 'Absent'},
    {'student_id': 103, 'attendance_date': '2024-03-06', 'status': 'Absent'},
    {'student_id': 103, 'attendance_date': '2024-03-07', 'status': 'Absent'},
    {'student_id': 103, 'attendance_date': '2024-03-08', 'status': 'Absent'},
    {'student_id': 104, 'attendance_date': '2024-03-09', 'status': 'Absent'},
    {'student_id': 104, 'attendance_date': '2024-03-01','status': 'Present'},    
    {'student_id': 104, 'attendance_date': '2024-03-02','status': 'Present'},
    {'student_id': 104, 'attendance_date': '2024-03-03','status': 'Absent'},
    {'student_id': 104, 'attendance_date': '2024-03-04','status': 'Present'},
    {'student_id': 104, 'attendance_date': '2024-03-05','status': 'Present'},
def find_absent_streaks(attendance_data):
    # Sort the data by student_id and attendance_date
    attendance_data.sort(key=lambda x: (x['student_id'], x['attendance_date']))
    
    # Dictionary to hold absence streaks
    absence_streaks = defaultdict(list)

    # Process attendance data
    for entry in attendance_data:
        student_id = entry['student_id']
        attendance_date = datetime.strptime(entry['attendance_date'], '%Y-%m-%d')
        status = entry['status']
        
        if status == 'Absent':
            if not absence_streaks[student_id] or absence_streaks[student_id][-1]['end_date'] + timedelta(days=1) != attendance_date:
                # Start a new streak
                absence_streaks[student_id].append({
                    'start_date': attendance_date,
                    'end_date': attendance_date,
                    'count': 1
                })
            else:
                # Extend the current streak
                streak = absence_streaks[student_id][-1]
                streak['end_date'] = attendance_date
                streak['count'] += 1

    # Prepare the output for students with streaks longer than 3 days
    result = []
    for student_id, streaks in absence_streaks.items():
        for streak in streaks:
            if streak['count'] > 3:
                result.append({
                    'student_id': student_id,
                    'absence_start_date': streak['start_date'].strftime('%Y-%m-%d'),
                    'absence_end_date': streak['end_date'].strftime('%Y-%m-%d'),
                    'total_absent_days': streak['count']
                })

    # Get the latest absence streak for each student
    latest_streaks = {}
    for entry in result:
        student_id = entry['student_id']
        if student_id not in latest_streaks or datetime.strptime(entry['absence_end_date'], '%Y-%m-%d') > datetime.strptime(latest_streaks[student_id]['absence_end_date'], '%Y-%m-%d'):
            latest_streaks[student_id] = entry

    return list(latest_streaks.values())

# Find and print the latest absence streaks
latest_absence_streaks = find_absent_streaks(attendance_data)
for streak in latest_absence_streaks:
    print(streak)x