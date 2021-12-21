import numpy as np
import cv2
import time
from .modules.face import FacePoints
from .modules.tracking import TrackPoints
from .modules.signal_processing import SignalProcess


def draw_str(dst, target, s):
    x, y = target
    cv2.putText(dst, s, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, 1.0,
                (0, 0, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN,
                1.0, (255, 255, 255), lineType=cv2.LINE_AA)


class Main:
    def __init__(self, path):

        self.bpm_arr = []
        self.path = path

    def capture_bpm(self):
        capture = cv2.VideoCapture(
            self.path)

        fps = int(capture.get(cv2.CAP_PROP_FPS))

        gray_frames = []  # 0 is newest -1 is oldest
        frame_c = 0

        face = FacePoints(dedector_type='haar')
        tracking = TrackPoints(
            face_dedector=face, max_trace_history=180, max_trace_num=60)
        signal = SignalProcess(tracking, fps, draw=False)

        # Create some random colors
        color = np.random.randint(0, 255, (100, 3))
        #cap_duration = 30
        #delay_time = 5
        bpm_arr = []
        #start_time = time.time()
        while (capture.isOpened()):
            # getting a frame
            ret, frame = capture.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            vis = frame.copy()

            gray_frames.insert(0, gray)

            # Wait 3 frames before selecting points
            if frame_c >= 3:
                # Keep most recent 3 gray frames
                gray_frames.pop()

                # Track Face points
                tracking.track_points(gray_frames[1], gray_frames[0])

                # Get longest trace
                longest_trace = max([len(trace)
                                     for trace in tracking.traces])

                # Draw points
                pts = tracking.get_current_points()
                for i, new in enumerate(pts):
                    a, b = new.ravel()
                    vis = cv2.circle(
                        vis, (a, b), 5, color[i % 100].tolist(), -1)

                # Draw Tracks
                cv2.polylines(vis, [np.int32(tr)
                                    for tr in tracking.traces], False, (0, 255, 0))

                draw_str(vis, (20, 100), 'trace lenght: %d' %
                         longest_trace)
                draw_str(vis, (20, 60), signal.graph_message)
                draw_str(vis, (20, 20), 'bpm: %d' % signal.mean_bpm)
                bpm_arr.append(signal.mean_bpm)

                # Only try to find BPM if trace len is longer then 3 seconds
                if longest_trace > 3*fps:
                    signal.find_bpm()

        # Show
            cv2.imshow('Signal Process', vis)

        # Break with esc key
            if cv2.waitKey(1) == 27:
                break

            frame_c += 1
        '''while (capture.isOpened() and int(time.time() - start_time) < cap_duration):
            if time.time() - start_time > delay_time:
                # getting a frame
                ret, frame = capture.read()
                if not ret:
                    break

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                vis = frame.copy()

                gray_frames.insert(0, gray)

                # Wait 3 frames before selecting points
                if frame_c >= 3:
                    # Keep most recent 3 gray frames
                    gray_frames.pop()

                    # Track Face points
                    tracking.track_points(gray_frames[1], gray_frames[0])

                    # Get longest trace
                    longest_trace = max([len(trace)
                                         for trace in tracking.traces])

                    # Draw points
                    pts = tracking.get_current_points()
                    for i, new in enumerate(pts):
                        a, b = new.ravel()
                        vis = cv2.circle(
                            vis, (a, b), 5, color[i % 100].tolist(), -1)

                    # Draw Tracks
                    cv2.polylines(vis, [np.int32(tr)
                                        for tr in tracking.traces], False, (0, 255, 0))

                    draw_str(vis, (20, 100), 'trace lenght: %d' %
                             longest_trace)
                    draw_str(vis, (20, 60), signal.graph_message)
                    draw_str(vis, (20, 20), 'bpm: %d' % signal.mean_bpm)
                    bpm_arr.append(signal.mean_bpm)

                    # Only try to find BPM if trace len is longer then 3 seconds
                    if longest_trace > 3*fps:
                        signal.find_bpm()

            # Show
            cv2.imshow('Signal Process', vis)

            # Break with esc key
            if cv2.waitKey(1) == 27:
                break

            frame_c += 1'''

        capture.release()
        cv2.destroyAllWindows()

        return (max(bpm_arr))


if __name__ == '__main__':
    Main.capture_bpm()
