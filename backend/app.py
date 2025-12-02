from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)

# Health check
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'message': 'Cyber Guardian API is running',
        'timestamp': datetime.now().isoformat()
    })

# Get predictions
@app.route('/api/predictions', methods=['GET'])
def get_predictions():
    predictions = [
        {
            'id': 1,
            'location': 'Connaught Place, Delhi',
            'risk': 94,
            'confidence': 89,
            'type': 'UPI Fraud',
            'amount': 230000,
            'predicted_time': '2h window',
            'lat': 28.6304,
            'lng': 77.2177
        },
        {
            'id': 2,
            'location': 'Bandra West, Mumbai',
            'risk': 87,
            'confidence': 85,
            'type': 'Phishing',
            'amount': 180000,
            'predicted_time': '3h window',
            'lat': 19.0596,
            'lng': 72.8295
        }
    ]
    return jsonify({'predictions': predictions, 'count': len(predictions)})

# Get alerts
@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    alerts = [
        {
            'id': 1,
            'location': 'Connaught Place, Delhi',
            'risk': 94,
            'time': '2 min ago',
            'type': 'UPI Fraud',
            'amount': '₹2.3L',
            'status': 'active'
        }
    ]
    return jsonify({'alerts': alerts})

# Get locations
@app.route('/api/locations', methods=['GET'])
def get_locations():
    locations = [
        {'name': 'SBI ATM, CP', 'lat': 28.6304, 'lng': 77.2177, 'risk': 94},
        {'name': 'HDFC Bank, Bandra', 'lat': 19.0596, 'lng': 72.8295, 'risk': 87}
    ]
    return jsonify({'locations': locations})

# Submit complaint
@app.route('/api/complaints', methods=['POST'])
def submit_complaint():
    data = request.get_json()
    return jsonify({
        'success': True,
        'message': 'Complaint submitted successfully',
        'complaint_id': 'CG2024001',
        'data': data
    })

if __name__ == '__main__':
    print('  Cyber Guardian API Starting...')
    print(' Running on http://localhost:5000')
    print(' API Endpoints:')
    print('   - GET  /api/health')
    print('   - GET  /api/predictions')
    print('   - GET  /api/alerts')
    print('   - GET  /api/locations')
    print('   - POST /api/complaints')
    app.run(debug=True, port=5000, host='0.0.0.0')
