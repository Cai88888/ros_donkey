
(cl:in-package :asdf)

(defsystem "multi_robot_traj_planner-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "PATH" :depends-on ("_package_PATH"))
    (:file "_package_PATH" :depends-on ("_package"))
  ))