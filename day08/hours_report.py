def read_sessions(path):
    sessions = []
    session = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                if session:
                    sessions.append(session)
                    session = []
            else:
                time_str, desc = line.split(' ', 1)
                h, m = time_str.split(':')
                minutes = int(h) * 60 + int(m)
                session.append((minutes, desc))
        if session:
            sessions.append(session)
    return sessions

def make_report(sessions):
    totals = {}       # description -> total minutes
    total_all = 0
    lines = []

    # detail lines
    for sess in sessions:
        for i in range(len(sess) - 1):
            start_min, desc = sess[i]
            end_min, _    = sess[i+1]
            dur = end_min - start_min
            # format back to HH:MM
            sh = start_min // 60
            sm = start_min % 60
            eh = end_min // 60
            em = end_min % 60
            lines.append(f"{sh:02d}:{sm:02d}-{eh:02d}:{em:02d} {desc}")
            if desc not in totals:
                totals[desc] = 0
            totals[desc] += dur
            total_all += dur
        lines.append("")  # blank between sessions

    # summary lines, sorted by largest first
    for desc, mins in sorted(totals.items(), key=lambda x: -x[1]):
        pct = round(mins * 100 / total_all)
        lines.append(f"{desc:25} {mins:4d} minutes   {pct:3d}%")

    return "\n".join(lines)

if __name__ == "__main__":
    sessions = read_sessions("timelog.log")
    report   = make_report(sessions)
    print(report)
