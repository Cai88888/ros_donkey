;; Auto-generated. Do not edit!


(when (boundp 'multi_robot_traj_planner::PATH)
  (if (not (find-package "MULTI_ROBOT_TRAJ_PLANNER"))
    (make-package "MULTI_ROBOT_TRAJ_PLANNER"))
  (shadow 'PATH (find-package "MULTI_ROBOT_TRAJ_PLANNER")))
(unless (find-package "MULTI_ROBOT_TRAJ_PLANNER::PATH")
  (make-package "MULTI_ROBOT_TRAJ_PLANNER::PATH"))

(in-package "ROS")
;;//! \htmlinclude PATH.msg.html


(defclass multi_robot_traj_planner::PATH
  :super ros::object
  :slots (_pathX _pathY _pathZ ))

(defmethod multi_robot_traj_planner::PATH
  (:init
   (&key
    ((:pathX __pathX) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:pathY __pathY) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:pathZ __pathZ) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _pathX __pathX)
   (setq _pathY __pathY)
   (setq _pathZ __pathZ)
   self)
  (:pathX
   (&optional __pathX)
   (if __pathX (setq _pathX __pathX)) _pathX)
  (:pathY
   (&optional __pathY)
   (if __pathY (setq _pathY __pathY)) _pathY)
  (:pathZ
   (&optional __pathZ)
   (if __pathZ (setq _pathZ __pathZ)) _pathZ)
  (:serialization-length
   ()
   (+
    ;; float32[] _pathX
    (* 4    (length _pathX)) 4
    ;; float32[] _pathY
    (* 4    (length _pathY)) 4
    ;; float32[] _pathZ
    (* 4    (length _pathZ)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _pathX
     (write-long (length _pathX) s)
     (dotimes (i (length _pathX))
       (sys::poke (elt _pathX i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _pathY
     (write-long (length _pathY) s)
     (dotimes (i (length _pathY))
       (sys::poke (elt _pathY i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;; float32[] _pathZ
     (write-long (length _pathZ) s)
     (dotimes (i (length _pathZ))
       (sys::poke (elt _pathZ i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _pathX
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _pathX (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _pathX i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _pathY
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _pathY (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _pathY i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;; float32[] _pathZ
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _pathZ (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _pathZ i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get multi_robot_traj_planner::PATH :md5sum-) "f4b6dd072e1420fea93c15a8167cfd2c")
(setf (get multi_robot_traj_planner::PATH :datatype-) "multi_robot_traj_planner/PATH")
(setf (get multi_robot_traj_planner::PATH :definition-)
      "float32[] pathX
float32[] pathY
float32[] pathZ
")



(provide :multi_robot_traj_planner/PATH "f4b6dd072e1420fea93c15a8167cfd2c")


