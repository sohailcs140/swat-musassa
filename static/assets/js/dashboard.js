/**
 *  Logistics Dashboard
 */

'use strict';

(function () {
  let labelColor, headingColor, currentTheme, bodyColor;

  if (isDarkStyle) {
    labelColor = config.colors_dark.textMuted;
    headingColor = config.colors_dark.headingColor;
    bodyColor = config.colors_dark.bodyColor;
    currentTheme = 'dark';
  } else {
    labelColor = config.colors.textMuted;
    headingColor = config.colors.headingColor;
    bodyColor = config.colors.bodyColor;
    currentTheme = 'light';
  }

  // Chart Colors
  const chartColors = {
    donut: {
      series1: config.colors.success,
      series2: '#43ff64e6',
      series3: '#43ff6473',
      series4: '#43ff6433'
    },
    line: {
      series1: config.colors.warning,
      series2: config.colors.primary,
      series3: '#7367f029'
    }
  };

  // Shipment statistics Chart
  // --------------------------------------------------------------------
  const shipmentEl = document.querySelector('#shipmentStatisticsChart'),
    shipmentConfig = {
      series: [
        {
          name: 'Shipment',
          type: 'column',
          data: [38, 45, 33, 38, 32, 50, 48, 40, 42, 37]
        },
        {
          name: 'Delivery',
          type: 'line',
          data: [23, 28, 23, 32, 28, 44, 32, 38, 26, 34]
        }
      ],
      chart: {
        height: 270,
        type: 'line',
        stacked: false,
        parentHeightOffset: 0,
        toolbar: {
          show: false
        },
        zoom: {
          enabled: false
        }
      },
      markers: {
        size: 4,
        colors: [config.colors.white],
        strokeColors: chartColors.line.series2,
        hover: {
          size: 6
        },
        borderRadius: 4
      },
      stroke: {
        curve: 'smooth',
        width: [0, 3],
        lineCap: 'round'
      },
      legend: {
        show: true,
        position: 'bottom',
        markers: {
          width: 8,
          height: 8,
          offsetX: -3
        },
        height: 40,
        offsetY: 10,
        itemMargin: {
          horizontal: 10,
          vertical: 0
        },
        fontSize: '15px',
        fontFamily: 'Inter',
        fontWeight: 400,
        labels: {
          colors: headingColor,
          useSeriesColors: false
        },
        offsetY: 10
      },
      grid: {
        strokeDashArray: 8
      },
      colors: [chartColors.line.series1, chartColors.line.series2],
      fill: {
        opacity: [1, 1]
      },
      plotOptions: {
        bar: {
          columnWidth: '30%',
          startingShape: 'rounded',
          endingShape: 'rounded',
          borderRadius: 4
        }
      },
      dataLabels: {
        enabled: false
      },
      xaxis: {
        tickAmount: 10,
        categories: ['1 Jan', '2 Jan', '3 Jan', '4 Jan', '5 Jan', '6 Jan', '7 Jan', '8 Jan', '9 Jan', '10 Jan'],
        labels: {
          style: {
            colors: labelColor,
            fontSize: '13px',
            fontFamily: 'Inter',
            fontWeight: 400
          }
        },
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        }
      },
      yaxis: {
        tickAmount: 4,
        min: 10,
        max: 50,
        labels: {
          style: {
            colors: labelColor,
            fontSize: '13px',
            fontFamily: 'Inter',
            fontWeight: 400
          },
          formatter: function (val) {
            return val + '%';
          }
        }
      },
      responsive: [
        {
          breakpoint: 1400,
          options: {
            chart: {
              height: 270
            },
            xaxis: {
              labels: {
                style: {
                  fontSize: '10px'
                }
              }
            },
            legend: {
              itemMargin: {
                vertical: 0,
                horizontal: 10
              },
              fontSize: '13px',
              offsetY: 12
            }
          }
        },
        {
          breakpoint: 1399,
          options: {
            chart: {
              height: 415
            },
            plotOptions: {
              bar: {
                columnWidth: '50%'
              }
            }
          }
        },
        {
          breakpoint: 982,
          options: {
            plotOptions: {
              bar: {
                columnWidth: '30%'
              }
            }
          }
        },
        {
          breakpoint: 480,
          options: {
            chart: {
              height: 250
            },
            legend: {
              offsetY: 7
            }
          }
        }
      ]
    };
  if (typeof shipmentEl !== undefined && shipmentEl !== null) {
    const shipment = new ApexCharts(shipmentEl, shipmentConfig);
    shipment.render();
  }

  // Reasons for delivery exceptions Chart
  // --------------------------------------------------------------------

const {total_visas, total_expire_visas,visas_expire_in_week,visas_expire_in_month} = JSON.parse((JSON.parse(document.getElementById("chart_data").textContent)).replace(/'/g, '"'))

console.log(chart_data)

  const deliveryExceptionsChartE1 = document.querySelector('#deliveryExceptionsChart'),
    deliveryExceptionsChartConfig = {
      chart: {
        height: 420,
        parentHeightOffset: 0,
        type: 'donut'
      },
      labels: [`Visa ${total_visas}`, `Expire Visas ${((total_expire_visas/total_visas)*100).toFixed(2)}%`,
      `Visas set to expire this week ${((visas_expire_in_week/total_visas)*100).toFixed(2)}%`, `Visas set to expire this month ${((visas_expire_in_month/total_visas)*100).toFixed(2)}%`],
      series: [total_visas, total_expire_visas, 
        visas_expire_in_week, visas_expire_in_month
      ],
      colors: [
        chartColors.donut.series1,
        chartColors.donut.series2,
        chartColors.donut.series3,
        chartColors.donut.series4
      ],
      stroke: {
        width: 0
      },
      dataLabels: {
        enabled: false,
        formatter: function (val, opt) {
          return parseInt(val);
        }
      },
      legend: {
        show: true,
        position: 'bottom',
        offsetY: 10,
        markers: {
          width: 8,
          height: 8,
          offsetX: -3
        },
        itemMargin: {
          horizontal: 15,
          vertical: 5
        },
        fontSize: '13px',
        fontFamily: 'Inter',
        fontWeight: 400,
        labels: {
          colors: headingColor,
          useSeriesColors: false
        }
      },
      tooltip: {
        theme: currentTheme
      },
      grid: {
        padding: {
          top: 15
        }
      },
      plotOptions: {
        pie: {
          donut: {
            size: '75%',
            labels: {
              show: true,
              value: {
                fontSize: '26px',
                fontFamily: 'Inter',
                color: headingColor,
                fontWeight: 500,
                offsetY: -30,
                formatter: function (val) {
                  return val;
                }
              },
              name: {
                offsetY: 20,
                fontFamily: 'Inter'
              },
              total: {
                show: true,
                fontSize: '0.9rem',
                label: 'Visas',
                color: bodyColor,
                formatter: function (w) {
                  return total_visas;
                }
              }
            }
          }
        }
      },
      responsive: [
        {
          breakpoint: 420,
          options: {
            chart: {
              height: 360
            }
          }
        }
      ]
    };
  if (typeof deliveryExceptionsChartE1 !== undefined && deliveryExceptionsChartE1 !== null) {
    const deliveryExceptionsChart = new ApexCharts(deliveryExceptionsChartE1, deliveryExceptionsChartConfig);
    deliveryExceptionsChart.render();
  }
})();



