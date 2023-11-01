; Auto-generated. Do not edit!


(cl:in-package multi_robot_traj_planner-msg)


;//! \htmlinclude PATH.msg.html

(cl:defclass <PATH> (roslisp-msg-protocol:ros-message)
  ((pathX
    :reader pathX
    :initarg :pathX
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (pathY
    :reader pathY
    :initarg :pathY
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0))
   (pathZ
    :reader pathZ
    :initarg :pathZ
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass PATH (<PATH>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PATH>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PATH)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name multi_robot_traj_planner-msg:<PATH> is deprecated: use multi_robot_traj_planner-msg:PATH instead.")))

(cl:ensure-generic-function 'pathX-val :lambda-list '(m))
(cl:defmethod pathX-val ((m <PATH>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader multi_robot_traj_planner-msg:pathX-val is deprecated.  Use multi_robot_traj_planner-msg:pathX instead.")
  (pathX m))

(cl:ensure-generic-function 'pathY-val :lambda-list '(m))
(cl:defmethod pathY-val ((m <PATH>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader multi_robot_traj_planner-msg:pathY-val is deprecated.  Use multi_robot_traj_planner-msg:pathY instead.")
  (pathY m))

(cl:ensure-generic-function 'pathZ-val :lambda-list '(m))
(cl:defmethod pathZ-val ((m <PATH>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader multi_robot_traj_planner-msg:pathZ-val is deprecated.  Use multi_robot_traj_planner-msg:pathZ instead.")
  (pathZ m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PATH>) ostream)
  "Serializes a message object of type '<PATH>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'pathX))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'pathX))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'pathY))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'pathY))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'pathZ))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-single-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)))
   (cl:slot-value msg 'pathZ))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PATH>) istream)
  "Deserializes a message object of type '<PATH>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'pathX) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'pathX)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'pathY) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'pathY)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'pathZ) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'pathZ)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-single-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PATH>)))
  "Returns string type for a message object of type '<PATH>"
  "multi_robot_traj_planner/PATH")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PATH)))
  "Returns string type for a message object of type 'PATH"
  "multi_robot_traj_planner/PATH")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PATH>)))
  "Returns md5sum for a message object of type '<PATH>"
  "f4b6dd072e1420fea93c15a8167cfd2c")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PATH)))
  "Returns md5sum for a message object of type 'PATH"
  "f4b6dd072e1420fea93c15a8167cfd2c")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PATH>)))
  "Returns full string definition for message of type '<PATH>"
  (cl:format cl:nil "float32[] pathX~%float32[] pathY~%float32[] pathZ~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PATH)))
  "Returns full string definition for message of type 'PATH"
  (cl:format cl:nil "float32[] pathX~%float32[] pathY~%float32[] pathZ~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PATH>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'pathX) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'pathY) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'pathZ) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 4)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PATH>))
  "Converts a ROS message object to a list"
  (cl:list 'PATH
    (cl:cons ':pathX (pathX msg))
    (cl:cons ':pathY (pathY msg))
    (cl:cons ':pathZ (pathZ msg))
))
