# -*- coding: utf-8 -*-
"""Professional Bicycle Racing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zNG_DL1cK_xKuXFBtkwwDIa4mbRdMP8Q
"""

from IPython.display import HTML
HTML("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Scatterplot Graph</title>
  <script src="https://d3js.org/d3.v7.min.js"></script>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background: #f4f4f4;
    }

    svg {
      background: white;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }

    .dot {
      fill: steelblue;
      opacity: 0.8;
    }

    .dot:hover {
      fill: orange;
    }

    #tooltip {
      position: absolute;
      background: rgba(0,0,0,0.7);
      color: #fff;
      padding: 8px;
      border-radius: 4px;
      font-size: 12px;
      pointer-events: none;
      opacity: 0;
      transition: opacity 0.2s;
    }
  </style>
</head>
<body>
  <h1 id="title">Doping in Professional Bicycle Racing</h1>
  <div id="tooltip"></div>
  <svg id="scatterplot" width="900" height="600"></svg>

  <script>
    const width = 900;
    const height = 600;
    const margin = { top: 60, right: 40, bottom: 60, left: 80 };

    const svg = d3.select("svg")
      .attr("width", width)
      .attr("height", height);

    const tooltip = d3.select("#tooltip");

    d3.json("https://raw.githubusercontent.com/freeCodeCamp/ProjectReferenceData/master/cyclist-data.json")
      .then(data => {
        const x = d3.scaleLinear()
          .domain([d3.min(data, d => d.Year - 1), d3.max(data, d => d.Year + 1)])
          .range([margin.left, width - margin.right]);

        const y = d3.scaleTime()
          .domain(d3.extent(data, d => new Date(Date.UTC(1970, 0, 1, 0, d.Seconds / 60, d.Seconds % 60))))
          .range([margin.top, height - margin.bottom]);

        // Axes
        const xAxis = d3.axisBottom(x).tickFormat(d3.format("d"));
        const yAxis = d3.axisLeft(y).tickFormat(d3.timeFormat("%M:%S"));

        svg.append("g")
          .attr("id", "x-axis")
          .attr("transform", `translate(0, ${height - margin.bottom})`)
          .call(xAxis);

        svg.append("g")
          .attr("id", "y-axis")
          .attr("transform", `translate(${margin.left}, 0)`)
          .call(yAxis);

        // Dots
        svg.selectAll(".dot")
          .data(data)
          .enter()
          .append("circle")
          .attr("class", "dot")
          .attr("cx", d => x(d.Year))
          .attr("cy", d => y(new Date(Date.UTC(1970, 0, 1, 0, d.Seconds / 60, d.Seconds % 60))))
          .attr("r", 6)
          .attr("data-xvalue", d => d.Year)
          .attr("data-yvalue", d => new Date(Date.UTC(1970, 0, 1, 0, d.Seconds / 60, d.Seconds % 60)))
          .style("fill", d => d.Doping ? "crimson" : "steelblue")
          .on("mouseover", function(event, d) {
            tooltip.style("opacity", 0.9)
              .attr("data-year", d.Year)
              .html(`${d.Name} (${d.Nationality})<br>Year: ${d.Year}, Time: ${d.Time}<br>${d.Doping}`)
              .style("left", (event.pageX + 10) + "px")
              .style("top", (event.pageY - 28) + "px");
          })
          .on("mouseout", () => tooltip.style("opacity", 0));

        // Legend
        const legend = svg.append("g")
          .attr("id", "legend")
          .attr("transform", `translate(${width - 200}, ${margin.top})`);

        legend.append("rect")
          .attr("x", 0).attr("y", 0)
          .attr("width", 20).attr("height", 20)
          .attr("fill", "crimson");

        legend.append("text")
          .attr("x", 30).attr("y", 15)
          .text("With Doping Allegations");

        legend.append("rect")
          .attr("x", 0).attr("y", 30)
          .attr("width", 20).attr("height", 20)
          .attr("fill", "steelblue");

        legend.append("text")
          .attr("x", 30).attr("y", 45)
          .text("No Doping Allegations");
      });
  </script>

  <script src="https://cdn.freecodecamp.org/testable-projects-fcc/v1/bundle.js"></script>
</body>
</html>
""")