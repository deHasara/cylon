/*
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef CYLON_SRC_CYLON_OPS_DIS_JOIN_OP_HPP_
#define CYLON_SRC_CYLON_OPS_DIS_JOIN_OP_HPP_
#include "ops/api/parallel_op.hpp"
#include "partition_op.hpp"
#include "join_op.hpp"

namespace cylon {

class DisJoinOpConfig {
 public:
  DisJoinOpConfig(PartitionOpConfig partition_config, join::config::JoinConfig join_config)
      : partition_config(std::move(partition_config)), join_config(join_config) {}

  PartitionOpConfig partition_config;
  join::config::JoinConfig join_config;
};

class DisJoinOP : public RootOp {
 public:
  const static int32_t LEFT_RELATION = 100;
  const static int32_t RIGHT_RELATION = 200;

  DisJoinOP(const std::shared_ptr<CylonContext> &ctx,
            const std::shared_ptr<arrow::Schema> &schema,
            int id,
            const ResultsCallback &callback,
            const DisJoinOpConfig &config);

  bool Execute(int tag, std::shared_ptr<Table> &table) override;
};
}

#endif //CYLON_SRC_CYLON_OPS_DIS_JOIN_OP_HPP_
