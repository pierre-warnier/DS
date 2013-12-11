function [sr, sc] = chisimk_full(m, it, sr, sc, k, p)
    % If k == 1: chisim
    % k: norm
    % p: pruning, ratio
    % sr = speye(size(m, 1));
    % sc = speye(size(m, 2));

    m = m .^ k;
    for i=1:it
       i,
       tic, [sr, sc] = inner_chisimk(m, sr, sc, k, p); toc,  
       max(max(sr)),
    end
    
end

function [sr, sc] = inner_chisimk(m, sr, sc, k, p)
    sc_old = sc;
    sc = prune(seteye(normalize01(normalize_chisimk(m' * sr     * m , k)), 1), p);
    sr = prune(seteye(normalize01(normalize_chisimk(m  * sc_old * m', k)), 1), p);
end
  
function m = normalize_chisimk(m, k)
    m = m .^ (1 / k);
    d = diag(m);
    d(d == 0) = 1;
    dd = 1 ./ d;
    m = m .* sqrt(dd * dd' .* (m > 0));
end