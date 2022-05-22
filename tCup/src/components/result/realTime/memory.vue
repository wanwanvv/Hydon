<template>
  <div>
    <el-container>
      <el-header height="2%" width="100%"></el-header>
      <el-main width="100%" height="100%">
        <div class="TopBox" id="graph1"></div>
        <div class="BottomBox_left" id="graph2"></div>
        <div class="BottomBox_middle" id="graph3"></div>
        <div class="BottomBox_right" id="graph4"></div>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Vue from "vue";

export default {
  name: 'memory',
  data() {
    return {
      APP_info: [0,0,0,0,0,0],
      BASE_info: [0,0,0,0,0,0,0,0,0,0,0]
    }
  },
  methods:{
    myEcharts( myChart_L1, dataset){
      var xid = [];
      var numSlice = 30;
      var lenSlice = 1;

      for( var i = 0; i < numSlice*lenSlice; i++) {
        xid.push(((numSlice*lenSlice-i)/lenSlice).toString()+'秒前');
      }
      xid.splice(numSlice*lenSlice-1,1,'现在');

      var option = {
        animation: false,
        grid: {
          x: 40,
          y: 50,
          x2: 40,
          y2: 30  //图表下方空白部分高度
        },
        title: {
          top: '3%',
          left: 'center',
          text: '内存占用率',
          textStyle: {
            color: '#FFF',
          },
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            animation: false
          },
          appendToBody:true,
          formatter: function (params) {
            return params[0].name + "内存的占用率："+params[0].value+"%";
          }
        },
        xAxis: [{
          show: true,
          type: 'category',
          boundaryGap: false,
          data: xid,
          axisLine: {
            lineStyle: {
              type: 'solid',
              color: '#eeeeee',//左边线的颜色
            }
          },
          axisLabel: {
            textStyle: {
              color: '#eeeeee',//坐标值得具体的颜色
            },
            interval: xid.length/5 - 1,
            showMaxLabel: true
          }
        }],
        yAxis: [{
          type: 'value',
          axisLine: {
            lineStyle: {
              type: 'solid',
              color: '#eeeeee',//左边线的颜色
            }
          },
          axisLabel: {
            textStyle: {
              color: '#eeeeee',//坐标值得具体的颜色
            },
            formatter:'{value}%',
          }
        }],
        series: [
          {
            name: '实时值',
            type: 'line',
            showSymbol: false,
            data: dataset,
            color: '#409EFF',
            //areaStyle: {}
          }]
      }
      myChart_L1.setOption(option);
    },
    myGraph1( myGraph){
      //var numset = [2355560448,3770613760,1196883968,1600061440,262144,1008664576,46333952,403767296];
      var numset = [parseFloat((parseFloat(this.BASE_info.used)/Math.pow(2,30)).toFixed(3)),
        parseFloat((parseFloat(this.BASE_info.free)/Math.pow(2,30)).toFixed(3)),
        parseFloat((parseFloat(this.BASE_info.active)/Math.pow(2,30)).toFixed(3)),
        parseFloat((parseFloat(this.BASE_info.inactive)/Math.pow(2,30)).toFixed(3)),
        parseFloat((parseFloat(this.BASE_info.buffers)/Math.pow(2,30)).toFixed(3)),
        parseFloat((parseFloat(this.BASE_info.cached)/Math.pow(2,30)).toFixed(3)),
        parseFloat((parseFloat(this.BASE_info.shared)/Math.pow(2,30)).toFixed(3)),
        parseFloat((parseFloat(this.BASE_info.slab)/Math.pow(2,30)).toFixed(3))]
      var option = {
        grid: {
          x: 50,
          y: 50,
          x2: 50,
          y2: 40,
        },
        tooltip: {
          show:true,
          appendToBody:true,
          formatter(params){
            //console.log(params);
            var names = ["当前已用的内存量","当前可用的内存量","当前活跃的内存量","当前非活跃的内存量","buffers","cached","共享内存量","slab"];
            return names[params.dataIndex]+": "+numset[params.dataIndex]+"G";
          }
        },
        title: {
          top: '5%',
          left: 'center',
          text: '内存各分区容量情况',
          textStyle: {
            color: '#FFF',
          },
        },
        xAxis: {
          type: 'category',
          data: ['used', 'free', 'active', 'inactive','buffers','cached', 'shared', 'slab'],
          axisLabel:{
            show:true,
            interval:0,
            rotate:45
          },
          axisLine: {
            lineStyle: {
              type: 'solid',
              color: '#eeeeee',//左边线的颜色
            }
          },
        },
        yAxis: {
          type: 'value',
          axisLabel:{
            formatter:'{value}G'
          },
          axisLine: {
            lineStyle: {
              type: 'solid',
              color: '#eeeeee',//左边线的颜色
            }
          },
        },
        series: [{
          name: 'cpu use time',
          data: numset,
          type: 'bar',
          color:'#aa88f8',
          barWidth:20
        }]
      };
      // 使用刚指定的配置项和数据显示图表。
      myGraph.setOption(option);//})
    },
    myGraph2( myGraph){
      var option = {
        color:['#ff5300','#ff9700'],
        tooltip: {
          trigger: 'item',
          appendToBody:true,
          formatter: '{b} : {c}KB'
        },
        title: {
          top: '5%',
          left: 'center',
          text: '当前活跃的内存情况分布',
          textStyle: {
            color: '#FFF',
          },
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          left: '70%',
          right: '3%',
          top: '40%',
          bottom: 20,
          textStyle: {
            color: '#FFF',
          },
        },
        series: [
          {
            name: '当前活跃的内存情况分布',
            type: 'pie',
            radius: ['40%', '70%'],
            center: ['38%','55%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              {value: parseFloat(this.APP_info.active_anon)/Math.pow(2,10), name: 'active_anon'},
              {value: parseFloat(this.APP_info.active_file)/Math.pow(2,10), name: 'active_file'}
            ]
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myGraph.setOption(option);//})
    },
    myGraph3( myGraph){
      var option = {
        color:['#e9003a','#00ab6f'],
        tooltip: {
          trigger: 'item',
          appendToBody:true,
          formatter: '{b} : {c}KB'
        },
        title: {
          top: '5%',
          left: 'center',
          text: '当前非活跃的内存情况分布',
          textStyle: {
            color: '#FFF',
          },
        },
        legend: {
          type: 'scroll',
          orient: 'vertical',
          left: '70%',
          right: '3%',
          top: '40%',
          bottom: 20,
          textStyle: {
            color: '#FFF',
          },
        },
        series: [
          {
            name: '当前非活跃的内存情况分布',
            type: 'pie',
            radius: ['40%', '70%'],
            center: ['38%','55%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: '40',
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              {value: parseFloat(this.APP_info.inactive_anon)/Math.pow(2,10), name: 'inactive_anon'},
              {value: parseFloat(this.APP_info.inactive_file)/Math.pow(2,10), name: 'inactive_file'}
            ]
          }
        ]
      };
      // 使用刚指定的配置项和数据显示图表。
      myGraph.setOption(option);//})
    },
    getData() {
      let lineGraph = this.$echarts.init(document.getElementById('graph1'));
      let divGraph = this.$echarts.init(document.getElementById('graph2'));
      let activeGraph = this.$echarts.init(document.getElementById('graph3'));
      let inactGraph = this.$echarts.init(document.getElementById('graph4'));
      let _this = this;

      var numset1 = [];
      var numSlice = 30;
      var lenSlice = 1;
      for( var i = 0; i < numSlice*lenSlice; i++) numset1.push(0);

      const CancelToken = this.$axios.CancelToken

      async function chartsInit() {
        await _this.$axios.get('api/monitor/status',{
          cancelToken: new CancelToken(function executor (c) {
            Vue.$httpRequestList.push(c)
          })
        }).then((res) => {
          //console.log('running memory...');
            _this.APP_info = res.data.memory_data.appendix_info;
            _this.BASE_info = res.data.memory_data.basic_info;
            //console.log(_this.DISK_io,_this.DISK_usage)
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
        //console.log(_this.CPU_time);

        for( var i = 0; i < lenSlice; i++) {
          numset1.push(parseFloat(_this.BASE_info.percent));
          //console.log(ii);
        }
        numset1.splice(0,lenSlice);

        _this.myEcharts( lineGraph, numset1);
        _this.myGraph1( divGraph);
        _this.myGraph2( activeGraph);
        _this.myGraph3( inactGraph);
      }
      chartsInit();

      this.timer = setInterval( function() {
        chartsInit();
      },1000)

      window.onresize = function(){
        lineGraph.resize();
        divGraph.resize();
        activeGraph.resize();
        inactGraph.resize();
      }
    }
  },
  mounted() {
    this.getData();
  },
  beforeDestroy() {
    if (this.timer) {
      clearInterval(this.timer); // 在Vue实例销毁前，清除我们的定时器
    }
  }
}
</script>

<style scoped>
.el-container {
  padding: 0;
  margin: 0;
  height: calc(100vh - 142px);
}
.el-aside {
  padding: 0;
  margin: 0;
  color: #333;
  height: 100%;
}
.el-main {
  padding: 0;
  margin: 0;
  height: 100%;
  width: 100%
}
/deep/ .el-table--enable-row-hover .el-table__body tr:hover>td {
  background-color: #409EFF;
  color: white;
}
.TopBox {
  width: 90%;
  margin-right: 1%;
  margin-top: 1%;
  height: 45%;
  border: 1px solid rgb(68,68,68);
  border-radius: 10px;
  box-shadow: 0 2px 5px black
}
.BottomBox_left{
  float: left;
  width: 28%;
  margin-right: 1.2%;
  margin-top: 2%;
  height: 45%;

  border: 1px solid rgb(68,68,68);
  border-radius: 10px;
  box-shadow: 0 2px 5px black
}
.BottomBox_middle{
  float: left;
  width: 28%;
  margin-left: 1.2%;
  margin-right: 1.2%;
  margin-top: 2%;
  height: 45%;

  border: 1px solid rgb(68,68,68);
  border-radius: 10px;
  box-shadow: 0 2px 5px black
}
.BottomBox_right{
  float: right;
  width: 28%;
  margin-left: 1.2%;
  margin-right: 10%;
  margin-top: 2%;
  height: 45%;

  border: 1px solid rgb(68,68,68);
  border-radius: 10px;
  box-shadow: 0 2px 5px black
}
</style>
