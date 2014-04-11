/*********************************************************************
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2013, JSK Lab
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/o2r other materials provided
 *     with the distribution.
 *   * Neither the name of the Willow Garage nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 *********************************************************************/

#include <pluginlib/class_list_macros.h>
#include "jsk_topic_tools/lightweight_throttle_nodelet.h"

namespace jsk_topic_tools
{
  void LightweightThrottle::onInit()
  {
    ros::NodeHandle nh = this->getPrivateNodeHandle();
    advertised_ = false;
    nh.param("update_rate", update_rate_, 1.0); // default 1.0
    sub_ = SubscriberPtr(new ros::Subscriber(
                           nh.subscribe("input", 1,
                                        &LightweightThrottle::inCallback,
                                        this,
                                        th_)));
  }

  void LightweightThrottle::inCallback(const ShapeShifterEvent& msg_event)
  {
    boost::shared_ptr<topic_tools::ShapeShifter const> const &msg
      = msg_event.getConstMessage();
    boost::shared_ptr<const ros::M_string> const& connection_header
      = msg_event.getConnectionHeaderPtr();

    // advertise if not
    if (!advertised_) {
      pub_ = msg->advertise(this->getPrivateNodeHandle(),
                            "output", 1);
      advertised_ = true;
    }
    // publish the message to output topic only if any
    // subscriber is
    if (pub_.getNumSubscribers()) {
      pub_.publish(msg);
    }
    // sleep to block callback
    ros::Duration(1 / update_rate_).sleep();
  }
  
  
}
typedef jsk_topic_tools::LightweightThrottle LightweightThrottle;
PLUGINLIB_DECLARE_CLASS(jsk_topic_tools, LightweightThrottle,
                        LightweightThrottle, nodelet::Nodelet)
