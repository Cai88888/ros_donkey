// Auto-generated. Do not edit!

// (in-package multi_robot_traj_planner.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class PATH {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.pathX = null;
      this.pathY = null;
      this.pathZ = null;
    }
    else {
      if (initObj.hasOwnProperty('pathX')) {
        this.pathX = initObj.pathX
      }
      else {
        this.pathX = [];
      }
      if (initObj.hasOwnProperty('pathY')) {
        this.pathY = initObj.pathY
      }
      else {
        this.pathY = [];
      }
      if (initObj.hasOwnProperty('pathZ')) {
        this.pathZ = initObj.pathZ
      }
      else {
        this.pathZ = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PATH
    // Serialize message field [pathX]
    bufferOffset = _arraySerializer.float32(obj.pathX, buffer, bufferOffset, null);
    // Serialize message field [pathY]
    bufferOffset = _arraySerializer.float32(obj.pathY, buffer, bufferOffset, null);
    // Serialize message field [pathZ]
    bufferOffset = _arraySerializer.float32(obj.pathZ, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PATH
    let len;
    let data = new PATH(null);
    // Deserialize message field [pathX]
    data.pathX = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [pathY]
    data.pathY = _arrayDeserializer.float32(buffer, bufferOffset, null)
    // Deserialize message field [pathZ]
    data.pathZ = _arrayDeserializer.float32(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 4 * object.pathX.length;
    length += 4 * object.pathY.length;
    length += 4 * object.pathZ.length;
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'multi_robot_traj_planner/PATH';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'f4b6dd072e1420fea93c15a8167cfd2c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32[] pathX
    float32[] pathY
    float32[] pathZ
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PATH(null);
    if (msg.pathX !== undefined) {
      resolved.pathX = msg.pathX;
    }
    else {
      resolved.pathX = []
    }

    if (msg.pathY !== undefined) {
      resolved.pathY = msg.pathY;
    }
    else {
      resolved.pathY = []
    }

    if (msg.pathZ !== undefined) {
      resolved.pathZ = msg.pathZ;
    }
    else {
      resolved.pathZ = []
    }

    return resolved;
    }
};

module.exports = PATH;
