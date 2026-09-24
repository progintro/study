-- Give every table explicit relative column widths, so the LaTeX writer typesets
-- wrapping p{} columns instead of l columns that run off the page.
--
-- pandoc's gfm reader leaves pipe-table widths at "default" (it has no --columns
-- heuristic, unlike the pandoc-markdown reader), and a default-width column never
-- wraps: a glossary row with a one-line definition overflows the right margin. Each
-- column gets a share of the line proportional to its longest cell, square-rooted so
-- that one long column does not squeeze the others to nothing.

local function cell_len(cell)
  return utf8.len(pandoc.utils.stringify(cell.contents)) or 0
end

function Table(t)
  local n = #t.colspecs
  if n < 2 then return nil end
  for _, spec in ipairs(t.colspecs) do
    if spec[2] ~= nil and spec[2] ~= pandoc.ColWidthDefault and spec[2] > 0 then
      return nil
    end
  end
  local longest = {}
  for i = 1, n do longest[i] = 1 end
  local function scan(rows)
    for _, row in ipairs(rows) do
      for i, cell in ipairs(row.cells) do
        if i <= n then longest[i] = math.max(longest[i], cell_len(cell)) end
      end
    end
  end
  scan(t.head.rows)
  for _, body in ipairs(t.bodies) do scan(body.body) end
  local total, w = 0, {}
  for i = 1, n do w[i] = math.sqrt(longest[i]); total = total + w[i] end
  -- narrow tables stay narrow: at most the full line, proportional to content
  local sum = 0
  for i = 1, n do sum = sum + longest[i] end
  local scale = math.min(1, sum / 60) * 0.98
  for i = 1, n do t.colspecs[i][2] = w[i] / total * scale end
  return t
end
