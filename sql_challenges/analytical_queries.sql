-- =============================================================================
-- Laboratorio de Consultas SQL Avanzadas (MySQL / PostgreSQL)
-- Autor: Bryan Francisco López León (github.com/BRyanLopez23)
-- =============================================================================

-- 1. Top 5 clientes con mayor facturación anual usando INNER JOIN, GROUP BY y HAVING
SELECT
    c.id AS cliente_id,
    c.nombre_empresa,
    COUNT(o.id) AS total_ordenes,
    ROUND(SUM(d.cantidad * d.precio_unitario), 2) AS facturacion_total_usd
FROM clientes c
INNER JOIN ordenes o ON o.cliente_id = c.id
INNER JOIN detalle_ordenes d ON d.orden_id = o.id
WHERE o.estado = 'COMPLETADA'
  AND o.fecha_emision >= '2026-01-01'
GROUP BY c.id, c.nombre_empresa
HAVING SUM(d.cantidad * d.precio_unitario) > 1000.00
ORDER BY facturacion_total_usd DESC
LIMIT 5;

-- 2. Función de Ventana (Window Function): Ranking de productos más vendidos por categoría
SELECT
    p.categoria_id,
    p.nombre AS producto,
    SUM(d.cantidad) AS unidades_vendidas,
    RANK() OVER (
        PARTITION BY p.categoria_id
        ORDER BY SUM(d.cantidad) DESC
    ) AS ranking_en_categoria
FROM productos p
INNER JOIN detalle_ordenes d ON d.producto_id = p.id
GROUP BY p.categoria_id, p.id, p.nombre;

-- 3. CTE (Common Table Expression): Detección de productos sin rotación en los últimos 90 días
WITH ventas_recientes AS (
    SELECT DISTINCT d.producto_id
    FROM detalle_ordenes d
    INNER JOIN ordenes o ON o.id = d.orden_id
    WHERE o.fecha_emision >= CURRENT_DATE - INTERVAL 90 DAY
)
SELECT
    p.id,
    p.codigo_sku,
    p.nombre,
    p.stock_actual
FROM productos p
LEFT JOIN ventas_recientes vr ON vr.producto_id = p.id
WHERE vr.producto_id IS NULL
  AND p.stock_actual > 0
ORDER BY p.stock_actual DESC;
