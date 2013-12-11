function m = prune(m, ratio)
    if ratio > 1 - nnz(m) / numel(m)
        s = sort(nonzeros(m));
        m = m .* (m > s(end - floor(numel(m) * (1 - ratio))));
    end
end