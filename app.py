from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_seek_time(sequence):
    return sum(abs(sequence[i] - sequence[i-1]) for i in range(1, len(sequence)))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    head = int(data['head'])
    requests = [int(x.strip()) for x in data['requests'].split(',') if x.strip().isdigit()]
    algo = data['algo']
    seek_rate = float(data.get('seek_rate', 2.0)) # Default to 2ms per track
    max_track = 199 
    
    sequence = []
    
    if algo == 'FCFS':
        sequence = [head] + requests
        
    elif algo == 'SSTF':
        sequence = [head]
        reqs = list(requests)
        curr = head
        while reqs:
            closest = min(reqs, key=lambda x: abs(x - curr))
            sequence.append(closest)
            reqs.remove(closest)
            curr = closest
            
    elif algo == 'SCAN':
        reqs = sorted(requests)
        left = [r for r in reqs if r < head]
        right = [r for r in reqs if r >= head]
        sequence = [head] + right + [max_track] + left[::-1]
        
    elif algo == 'C-SCAN':
        reqs = sorted(requests)
        left = [r for r in reqs if r < head]
        right = [r for r in reqs if r >= head]
        if not right and not left:
            sequence = [head]
        else:
            sequence = [head] + right + [max_track, 0] + left
            
    elif algo == 'LOOK':
        reqs = sorted(requests)
        left = [r for r in reqs if r < head]
        right = [r for r in reqs if r >= head]
        sequence = [head] + right + left[::-1]
        
    elif algo == 'C-LOOK':
        reqs = sorted(requests)
        left = [r for r in reqs if r < head]
        right = [r for r in reqs if r >= head]
        sequence = [head] + right + left

    # --- New Calculations ---
    total_movement = calculate_seek_time(sequence)
    num_requests = len(requests)
    
    # Average seek distance per request
    avg_seek = round(total_movement / num_requests, 2) if num_requests > 0 else 0
    
    # Estimated time = Total distance * speed (ms/track)
    total_time_ms = round(total_movement * seek_rate, 2)
    
    return jsonify({
        'sequence': sequence,
        'total_movement': total_movement,
        'avg_seek': avg_seek,
        'total_time_ms': total_time_ms
    })

if __name__ == '__main__':
    app.run(debug=True)